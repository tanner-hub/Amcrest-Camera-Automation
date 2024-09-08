# -*- coding: utf-8 -*-
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# vim:sw=4:ts=4:et

from amcrest import AmcrestCamera

amcrest = AmcrestCamera('192.168.1.10', 80, 'admin', 'super_password')
camera = amcrest.camera

camera.snapshot(channel=0, path_file="/tmp/snapshot.jpg")
