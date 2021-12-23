#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2018-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
import numpy

digits = numpy.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x0b, 0x96, 0xfd, 0xca, 0x1f, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0x25, 0xfb, 0xfb, 0xfd, 0x6b, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0x15, 0xc5, 0xfb, 0xfb, 0xfd, 0x6b, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x6e, 0xbe, 0xfb,
                       0xfb, 0xfb, 0xfd, 0xa9, 0x6d, 0x3e, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0xfd, 0xfb, 0xfb, 0xfb, 0xfb, 0xfd, 0xfb, 0xfb, 0xdc, 0x33, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xb6, 0xff, 0xfd, 0xfd, 0xfd,
                       0xfd, 0xea, 0xde, 0xfd, 0xfd, 0xfd, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0x3f, 0xdd, 0xfd, 0xfb, 0xfb, 0xfb, 0x93, 0x4d, 0x3e, 0x80, 0xfb, 0xfb, 0x69, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x20, 0xe7, 0xfb, 0xfd, 0xfb, 0xdc, 0x89, 0x0a,
                       0, 0, 0x1f, 0xe6, 0xfb, 0xf3, 0x71, 0x05, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0x25, 0xfb, 0xfb, 0xfd, 0xbc, 0x14, 0, 0, 0, 0, 0, 0x6d, 0xfb, 0xfd, 0xfb, 0x23, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x25, 0xfb, 0xfb, 0xc9, 0x1e, 0, 0, 0, 0,
                       0, 0, 0x1f, 0xc8, 0xfd, 0xfb, 0x23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0x25, 0xfd, 0xfd, 0, 0, 0, 0, 0, 0, 0, 0, 0x20, 0xca, 0xff, 0xfd, 0xa4, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0x8c, 0xfb, 0xfb, 0, 0, 0, 0, 0, 0, 0,
                       0, 0x6d, 0xfb, 0xfd, 0xfb, 0x23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xd9,
                       0xfb, 0xfb, 0, 0, 0, 0, 0, 0, 0x15, 0x3f, 0xe7, 0xfb, 0xfd, 0xe6, 0x1e, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0xd9, 0xfb, 0xfb, 0, 0, 0, 0, 0, 0, 0x90, 0xfb,
                       0xfb, 0xfb, 0xdd, 0x3d, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xd9, 0xfb,
                       0xfb, 0, 0, 0, 0, 0, 0xb6, 0xdd, 0xfb, 0xfb, 0xfb, 0xb4, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0xda, 0xfd, 0xfd, 0x49, 0x49, 0xe4, 0xfd, 0xfd, 0xff, 0xfd, 0xfd, 0xfd,
                       0xfd, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x71, 0xfb, 0xfb,
                       0xfd, 0xfb, 0xfb, 0xfb, 0xfb, 0xfd, 0xfb, 0xfb, 0xfb, 0x93, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0x1f, 0xe6, 0xfb, 0xfd, 0xfb, 0xfb, 0xfb, 0xfb, 0xfd, 0xe6, 0xbd, 0x23, 0x0a,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x3e, 0x8e, 0xfd,
                       0xfb, 0xfb, 0xfb, 0xfb, 0xfd, 0x6b, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0x48, 0xae, 0xfb, 0xad, 0x47, 0x48, 0x1e, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0],

                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x26, 0xfe, 0x6d, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x57, 0xfc, 0x52, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x87, 0xf1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x2d, 0xf4, 0x96, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x54, 0xfe, 0x3f, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xca, 0xdf, 0x0b, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x20, 0xfe, 0xd8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x5f, 0xfe, 0xc3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x8c, 0xfe, 0x4d, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x39, 0xed, 0xcd, 0x08, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x7c, 0xff, 0xa5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xab, 0xfe, 0x51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x18, 0xe8, 0xd7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x78, 0xfe, 0x9f, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x97, 0xfe, 0x8e, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xe4, 0xfe, 0x42, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x3d, 0xfb, 0xfe, 0x42, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x8d, 0xfe, 0xcd, 0x03, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x0a, 0xd7, 0xfe, 0x79, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x05, 0xc6, 0xb0, 0x0a, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x74,
                       0x7d, 0xab, 0xff, 0xff, 0x96, 0x5d, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0xa9, 0xfd, 0xfd, 0xfd, 0xfd, 0xfd, 0xfd, 0xda, 0x1e, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xa9, 0xfd, 0xfd, 0xfd,
                       0xd5, 0x8e, 0xb0, 0xfd, 0xfd, 0x7a, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0x34, 0xfa, 0xfd, 0xd2, 0x20, 0x0c, 0, 0x06, 0xce, 0xfd, 0x8c, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x4d, 0xfb, 0xd2, 0x19, 0, 0,
                       0, 0x7a, 0xf8, 0xfd, 0x41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0x1f, 0x12, 0, 0, 0, 0, 0xd1, 0xfd, 0xfd, 0x41, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x75,
                       0xf7, 0xfd, 0xc6, 0x0a, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0x4c, 0xf7, 0xfd, 0xe7, 0x3f, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x80, 0xfd, 0xfd,
                       0x90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0xb0, 0xf6, 0xfd, 0x9f, 0x0c, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x19, 0xea, 0xfd, 0xe9, 0x23, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0xc6, 0xfd, 0xfd, 0x8d, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x4e, 0xf8, 0xfd, 0xbd, 0x0c, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0x13, 0xc8, 0xfd, 0xfd, 0x8d, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0x86, 0xfd, 0xfd, 0xad, 0x0c, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xf8,
                       0xfd, 0xfd, 0x19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0xf8, 0xfd, 0xfd, 0x2b, 0x14, 0x14, 0x14, 0x14, 0x05, 0, 0x05,
                       0x14, 0x14, 0x25, 0x96, 0x96, 0x96, 0x93, 0x0a, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xf8, 0xfd,
                       0xfd, 0xfd, 0xfd, 0xfd, 0xfd, 0xfd, 0xa8, 0x8f, 0xa6, 0xfd, 0xfd, 0xfd, 0xfd, 0xfd, 0xfd, 0xfd, 0x7b, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0xae, 0xfd, 0xfd, 0xfd, 0xfd, 0xfd, 0xfd, 0xfd, 0xfd, 0xfd, 0xfd, 0xfd,
                       0xf9, 0xf7, 0xf7, 0xa9, 0x75, 0x75, 0x39, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x76, 0x7b,
                       0x7b, 0x7b, 0xa6, 0xfd, 0xfd, 0xfd, 0x9b, 0x7b, 0x7b, 0x29, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0],

                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0x15, 0x71, 0xc1, 0xfe, 0xfd, 0xfe, 0xfd, 0xfe, 0xac, 0x52, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xb7, 0xfd, 0xfc, 0xfd, 0xfc, 0xfd,
                       0xfc, 0xfd, 0xfc, 0xf3, 0x28, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0xcb, 0xff, 0xe9, 0xb7, 0x66, 0xcb, 0xcb, 0xea, 0xfd, 0xfe, 0x97, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x51, 0x97, 0x32, 0, 0, 0, 0x29,
                       0xc1, 0xfc, 0xfd, 0x6f, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0x0b, 0xd5, 0xfe, 0xfd, 0xcb, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x7b, 0xd5, 0xfc, 0xfd,
                       0xfc, 0x51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0x33, 0xfd, 0xfe, 0xfd, 0xfe, 0x97, 0x15, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x0a, 0xd4, 0xfd, 0xfc, 0xfd, 0xe8,
                       0xdf, 0x7a, 0x52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0x7b, 0xdf, 0xfe, 0xfd, 0xfe, 0xfd, 0xfe, 0x47, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x14, 0x32, 0x83, 0xd5,
                       0xfc, 0xfd, 0xc0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0x15, 0xa2, 0xfe, 0xfd, 0x66, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x15, 0xcb,
                       0xfd, 0xfc, 0x3d, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0x84, 0xfd, 0xfe, 0x5b, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x15, 0x8e, 0xfd, 0xfc, 0xe9,
                       0x1e, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0x29, 0xd6, 0xfd, 0xfe, 0xd5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xa3, 0xf3, 0xfd, 0xfc, 0xac, 0x0a, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x0b, 0xad, 0xad,
                       0xfd, 0xff, 0xfd, 0xe0, 0x51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0x84, 0xfc, 0xfd, 0xfc, 0xfd, 0xab, 0x14, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x99, 0xfd, 0xf4, 0xcb,
                       0x52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0x5c, 0xc0, 0x7a, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0],

                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x32, 0xe0,
                       0, 0, 0, 0, 0, 0, 0, 0x46, 0x1d, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0x79, 0xe7, 0, 0, 0, 0, 0, 0, 0, 0x94, 0xa8, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x04, 0xc3, 0xe7, 0,
                       0, 0, 0, 0, 0, 0, 0x60, 0xd2, 0x0b, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0x45, 0xfc, 0x86, 0, 0, 0, 0, 0, 0, 0, 0x72, 0xfc, 0x15, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x2d, 0xec, 0xd9, 0x0c, 0, 0,
                       0, 0, 0, 0, 0, 0xc0, 0xfc, 0x15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0xa8, 0xf7, 0x35, 0, 0, 0, 0, 0, 0, 0, 0x12, 0xff, 0xfd, 0x15, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x54, 0xf2, 0xd3, 0, 0, 0, 0, 0,
                       0, 0, 0, 0x8d, 0xfd, 0xbd, 0x05, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0xa9, 0xfc, 0x6a, 0, 0, 0, 0, 0, 0, 0, 0x20, 0xe8, 0xfa, 0x42, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0x0f, 0xe1, 0xfc, 0, 0, 0, 0, 0, 0, 0,
                       0, 0x86, 0xfc, 0xd3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x16,
                       0xfc, 0xa4, 0, 0, 0, 0, 0, 0, 0, 0, 0xa9, 0xfc, 0xa7, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0x09, 0xcc, 0xd1, 0x12, 0, 0, 0, 0, 0, 0, 0x16,
                       0xfd, 0xfd, 0x6b, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xa9,
                       0xfc, 0xc7, 0x55, 0x55, 0x55, 0x55, 0x81, 0xa4, 0xc3, 0xfc, 0xfc, 0x6a, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0x29, 0xaa, 0xf5, 0xfc, 0xfc, 0xfc, 0xfc, 0xe8, 0xe7, 0xfb, 0xfc,
                       0xfc, 0x09, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0x31, 0x54, 0x54, 0x54, 0x54, 0, 0, 0xa1, 0xfc, 0xfc, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x7f, 0xfc, 0xfc,
                       0x2d, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0x80, 0xfd, 0xfd, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x7f, 0xfc, 0xfc, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0x87, 0xfc, 0xf4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xe8, 0xec, 0x6f, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0xb3, 0x42, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0],

                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x33, 0x84, 0xd6, 0xfd, 0xfe, 0xfd, 0xcb, 0xa2, 0x29,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x66, 0x8e, 0xcb, 0xcb,
                       0xfd, 0xfc, 0xfd, 0xfc, 0x97, 0x46, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0xfe, 0xfd, 0xf4, 0xcb, 0x8e, 0x66, 0x52, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xac, 0xfc, 0xcb, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0x15, 0xdf, 0xea, 0x1e, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x7a, 0xfd, 0x32, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0x7b, 0xfe, 0x5b, 0x33, 0x33, 0x33, 0x0a, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x15, 0xdf, 0xfd, 0xfc, 0xfd, 0xfc, 0xfd,
                       0xac, 0x52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0x15, 0xd6, 0xfd, 0xcb, 0xa2, 0x66, 0x66, 0xcb, 0xdf, 0xfe, 0xfd, 0x33, 0x0a, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x3d, 0xfd, 0xab, 0, 0, 0, 0, 0, 0x14,
                       0x70, 0xc0, 0xfd, 0xd4, 0x29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x66, 0xcb, 0xea, 0x33, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0x14, 0xd5, 0xe8, 0x52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x3e, 0xcb, 0xea, 0x70, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0x14, 0xd5, 0xfc, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x99, 0xfd, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0x29, 0xe9, 0xd4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x71, 0x5c,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x1f, 0xad, 0xf4, 0x28, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0x52, 0xfd, 0x97, 0, 0, 0, 0, 0, 0, 0x15, 0x66, 0x66, 0xb7,
                       0xe9, 0xd4, 0x51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x52, 0xff, 0xfd, 0xea,
                       0x98, 0x99, 0xc1, 0xad, 0xfd, 0xfe, 0xfd, 0xfe, 0xd5, 0x8e, 0x14, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0x47, 0x97, 0x97, 0xe8, 0xfd, 0xd4, 0xc0, 0x97, 0x83, 0x32, 0x32, 0x0a, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0],

                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x07,
                       0xcc, 0xfd, 0xb0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0x07, 0x96, 0xfc, 0xfc, 0x7d, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x75, 0xfc, 0xba,
                       0x38, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0x8d, 0xfc, 0x76, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x9a, 0xf7, 0x32, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0x1a, 0xfd, 0xc4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x96, 0xfd, 0xc4, 0, 0, 0,
                       0, 0, 0, 0, 0x39, 0x55, 0x55, 0x26, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0xe1, 0xfd, 0x60, 0, 0, 0, 0, 0, 0x97, 0xe2, 0xf3, 0xfc, 0xfc, 0xee, 0x7d, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x0a, 0xe5, 0xe2, 0, 0, 0, 0x04, 0x36,
                       0xe5, 0xfd, 0xff, 0xea, 0xaf, 0xe1, 0xff, 0xe4, 0x1f, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0x6e, 0xfc, 0x96, 0, 0, 0x1a, 0x80, 0xfc, 0xfc, 0xe3, 0x86, 0x1c, 0, 0, 0xb2, 0xfc, 0x38, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x9f, 0xfc, 0x71, 0, 0, 0x96, 0xfd, 0xfc, 0xba,
                       0x2b, 0, 0, 0, 0, 0x8d, 0xfc, 0x38, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0xb9, 0xfc, 0x71, 0, 0x26, 0xed, 0xfd, 0x97, 0x06, 0, 0, 0, 0, 0, 0x8d, 0xca, 0x06, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0xc6, 0xfd, 0x72, 0, 0x93, 0xfd, 0xa3, 0, 0, 0,
                       0, 0, 0, 0, 0x9a, 0xc5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xc5,
                       0xfc, 0x71, 0, 0xac, 0xfc, 0xbc, 0, 0, 0, 0, 0, 0, 0x1a, 0xfd, 0xab, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0xc5, 0xfc, 0x71, 0, 0x13, 0xe7, 0xf7, 0x7a, 0x13, 0, 0,
                       0, 0, 0xc8, 0xf4, 0x38, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x1a, 0xde, 0xfc,
                       0x71, 0, 0, 0x19, 0xcb, 0xfc, 0xc1, 0x0d, 0, 0x4c, 0xc8, 0xf9, 0x7d, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0xb9, 0xfd, 0xb3, 0x0a, 0, 0, 0, 0x4c, 0x23, 0x1d, 0x9a, 0xfd,
                       0xf4, 0x7d, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x1c, 0xd1, 0xfd,
                       0xc4, 0x52, 0x39, 0x39, 0x83, 0xc5, 0xfc, 0xfd, 0xd6, 0x51, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0x19, 0xd8, 0xfc, 0xfc, 0xfc, 0xfd, 0xfc, 0xfc, 0xfc, 0x9c, 0x13, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x10, 0x67,
                       0x8b, 0xf0, 0x8c, 0x8b, 0x8b, 0x28, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0],

                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x54, 0xb9, 0x9f, 0x97, 0x3c, 0x24, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0xde, 0xfe, 0xfe, 0xfe, 0xfe, 0xf1, 0xc6, 0xc6, 0xc6, 0xc6, 0xc6, 0xc6, 0xc6, 0xc6, 0xaa, 0x34, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x43, 0x72, 0x48, 0x72, 0xa3, 0xe3, 0xfe, 0xe1,
                       0xfe, 0xfe, 0xfe, 0xfa, 0xe5, 0xfe, 0xfe, 0x8c, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0x11, 0x42, 0x0e, 0x43, 0x43, 0x43, 0x3b, 0x15, 0xec, 0xfe, 0x6a, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0x53, 0xfd, 0xd1, 0x12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x16, 0xe9, 0xff, 0x53, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0x81, 0xfe, 0xee, 0x2c, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0x3b, 0xf9, 0xfe, 0x3e, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x85,
                       0xfe, 0xbb, 0x05, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0x09, 0xcd, 0xf8, 0x3a, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x7e, 0xfe, 0xb6,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0x4b, 0xfb, 0xf0, 0x39, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x13, 0xdd, 0xfe, 0xa6, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0x03, 0xcb, 0xfe, 0xdb, 0x23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x26, 0xfe, 0xfe, 0x4d, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0x1f, 0xe0, 0xfe, 0x73, 0x01, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0x85, 0xfe, 0xfe, 0x34, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x3d, 0xf2,
                       0xfe, 0xfe, 0x34, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0x79, 0xfe, 0xfe, 0xdb, 0x28, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x79, 0xfe, 0xcf,
                       0x12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0],

                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0x06, 0x4b, 0, 0x62, 0xb9, 0xb2, 0x5e, 0x13, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x0f, 0x6f, 0xc3, 0xee, 0x5e, 0, 0xd0, 0xf9, 0xfe,
                       0xfe, 0x74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x14, 0x32, 0x6b,
                       0xc5, 0xf6, 0xb7, 0x19, 0, 0, 0x51, 0xf5, 0xfe, 0xf9, 0x5b, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0x12, 0x54, 0xe6, 0xfe, 0xfe, 0xdd, 0x56, 0, 0, 0x01, 0x7d, 0xfd, 0xfe, 0xb2, 0x35,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x85, 0xfe, 0xfe, 0xd9, 0x76, 0x04,
                       0, 0, 0x3e, 0xca, 0xfe, 0xf1, 0x83, 0x08, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0x6b, 0xf4, 0xfe, 0xd5, 0x2d, 0, 0, 0, 0x3e, 0xf0, 0xfe, 0xdc, 0x1d, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x2c, 0xf6, 0xfe, 0xd1, 0x31, 0, 0, 0, 0x1f,
                       0xf1, 0xfe, 0xdd, 0x1b, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0x5f, 0xfe, 0xfe, 0x37, 0, 0, 0, 0x11, 0xc6, 0xfe, 0xda, 0x1c, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0x1b, 0xdb, 0xfe, 0xe9, 0x90, 0x27, 0x2a, 0xcc, 0xfe, 0xcd,
                       0x0a, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0x73, 0xf8, 0xfe, 0xfe, 0xf4, 0xe9, 0xfe, 0xdf, 0x18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x26, 0x54, 0xa8, 0xf5, 0xfe, 0xfe, 0xfe, 0xcf, 0x73,
                       0x09, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0x0e, 0xec, 0xfe, 0xe6, 0xa3, 0xed, 0xf4, 0xd3, 0x50, 0x01, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x63, 0xfe, 0xfe, 0x63, 0, 0, 0x25, 0xe1,
                       0xfe, 0x82, 0x08, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0x47, 0xfe, 0xe5, 0x0c, 0, 0, 0, 0x02, 0xaa, 0xfe, 0x33, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x60, 0xfe, 0xfe, 0x12, 0, 0, 0, 0, 0x51,
                       0xfe, 0xc6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0x50, 0xfe, 0xfe, 0x12, 0, 0, 0, 0, 0x83, 0xfe, 0x77, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0x05, 0xd6, 0xfe, 0x4e, 0, 0, 0, 0x01, 0xb7, 0xf4,
                       0x3f, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0x40, 0xfd, 0xdf, 0x18, 0, 0x02, 0x7e, 0xfe, 0xb2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x57, 0xee, 0xde, 0x77, 0xb1, 0xfe, 0xd9, 0x1b, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0x12, 0x9a, 0xc4, 0xc4, 0x65, 0x19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0],

                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0x24, 0x38, 0x89, 0xc9, 0xc7, 0x5f, 0x25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0x2d, 0x98, 0xea, 0xfe, 0xfe, 0xfe, 0xfe, 0xfe, 0xfa, 0xd3, 0x97, 0x06,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x2e, 0x99, 0xf0, 0xfe, 0xfe,
                       0xe3, 0xa6, 0x85, 0xfb, 0xc8, 0xfe, 0xe5, 0xe1, 0x68, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0x99, 0xea, 0xfe, 0xfe, 0xbb, 0x8e, 0x08, 0, 0, 0xbf, 0x28, 0xc6, 0xf6, 0xdf, 0xfd, 0x15,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x08, 0x7e, 0xfd, 0xfe, 0xe9, 0x80, 0x0b, 0, 0,
                       0, 0, 0xd2, 0x2b, 0x46, 0xfe, 0xfe, 0xfe, 0x15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0x48, 0xf3, 0xfe, 0xe4, 0x36, 0, 0, 0, 0, 0x03, 0x20, 0x74, 0xe1, 0xf2, 0xfe, 0xff, 0xa2, 0x05, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0x4b, 0xf0, 0xfe, 0xdf, 0x6d, 0x8a, 0xb2, 0xb2, 0xa9, 0xd2,
                       0xfb, 0xe7, 0xfe, 0xfe, 0xfe, 0xe8, 0x26, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x09,
                       0xaf, 0xf4, 0xfd, 0xff, 0xfe, 0xfe, 0xfb, 0xfe, 0xfe, 0xfe, 0xfe, 0xfe, 0xfc, 0xab, 0x19, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x10, 0x88, 0xc3, 0xb0, 0x92, 0x99, 0xc8, 0xfe, 0xfe,
                       0xfe, 0xfe, 0x96, 0x10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0xa2, 0xfe, 0xfe, 0xf1, 0x63, 0x03, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x76, 0xfa, 0xfe, 0xfe, 0x5a,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0x64, 0xf2, 0xfe, 0xfe, 0xd3, 0x07, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x36, 0xf1, 0xfe, 0xfe, 0xf2, 0x3b, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0x83, 0xfe, 0xfe, 0xf4, 0x40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0x0d, 0xf9, 0xfe, 0xfe, 0x98, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x0c, 0xe4,
                       0xfe, 0xfe, 0xd0, 0x08, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0x4e, 0xff, 0xfe, 0xfe, 0x42, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xd1, 0xfe, 0xfe,
                       0x89, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0xe3, 0xff, 0xe9, 0x19, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x71, 0xff, 0x6c, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0]])
