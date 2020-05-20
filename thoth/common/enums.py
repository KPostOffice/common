#!/usr/bin/env python3
# thoth-common
# Copyright(C) 2020 Francesco Murdaca
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Enum types used for Thoth adviser integrations."""

from enum import Enum


class ThothAdviserIntegrationEnum(Enum):
    """Class for Thoth Adviser integrations."""

    cli = "cli"
    kebechet = "kebechet"
    s2i = "s2i"
    github_app = "github_app"
    jypyter_notebook = "jypyter_notebook"