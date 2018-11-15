#!/bin/bash
#
# This file is part of the VSS-SDK project.
#
# This Source Code Form is subject to the terms of the GNU GENERAL PUBLIC LICENSE,
# v. 3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at http://www.gnu.org/licenses/gpl-3.0/.
#

protoc -I=. --python_out=. protos/state.proto
protoc -I=. --python_out=. protos/command.proto
protoc -I=. --python_out=. protos/debug.proto
protoc -I=. --python_out=. protos/control.proto

mkdir -p src/protos

mv protos/*_pb2.py src/protos