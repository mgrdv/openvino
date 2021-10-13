// Copyright (C) 2018-2021 Intel Corporation
// SPDX-License-Identifier: Apache-2.0
//

#pragma once

#include "openvino/core/function.hpp"

namespace ov {
namespace preprocess {

/// \brief Internal guard to make preprocess builder exception-safe
class FunctionGuard {
    std::shared_ptr<Function> m_function;
    ParameterVector m_parameters;
    std::map<std::shared_ptr<op::v0::Parameter>, std::set<Input<Node>>> m_backup;
    bool m_done = false;

public:
    FunctionGuard(const std::shared_ptr<Function>& f) : m_function(f) {
        m_parameters = f->get_parameters();
        for (const auto& param : f->get_parameters()) {
            m_backup.insert({param, param->output(0).get_target_inputs()});
        }
    }
    virtual ~FunctionGuard() {
        if (!m_done) {
            try {
                auto params = m_function->get_parameters();
                // Remove parameters added by preprocessing
                for (const auto& param : params) {
                    m_function->remove_parameter(param);
                }
                // Insert old parameters and update consumers
                for (const auto& item : m_backup) {
                    // Replace consumers
                    for (auto consumer : item.second) {
                        consumer.replace_source_output(item.first);
                    }
                }
                m_function->add_parameters(m_parameters);
            } catch (std::exception& ex) {
                // Stress condition, can't recover function to original state
                std::cerr << "Unrecoverable error occurred during preprocessing. Function is corrupted, exiting\n";
                exit(EXIT_FAILURE);
            }
        }
    }
    void reset() noexcept {
        m_done = true;
    }
};

}  // namespace preprocess
}  // namespace ov