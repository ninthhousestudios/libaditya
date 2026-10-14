# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Ninth House Studios LLC

#    libaditya is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    libaditya is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#    You should have received a copy of the GNU Affero General Public License
#    along with libaditya.  If not, see <https://www.gnu.org/licenses/>.

# Optional dependencies live in pyproject extras and are imported lazily at
# their point of use. When one is missing, this finder turns the bare
# "No module named 'rich'" into an error naming the extra to install.
#
# It sits at the END of sys.meta_path, so it is only consulted after every
# real finder has failed: an installed package is never affected, and the
# error raised is still a ModuleNotFoundError, so `except ImportError`
# fallbacks behave exactly as before.

import sys

# top-level module -> (extra, what libaditya uses it for)
OPTIONAL_MODULES = {
    "rich": ("print", "terminal tables (.rich(), print_functions)"),
    "prettytable": ("print", "terminal tables (.print(), print_functions)"),
    "drawsvg": ("draw", "SVG drawing (bodygraph, sarvatobhadra chakra)"),
    "metar": ("weather", "METAR weather lookup"),
    "requests": ("stellarium", "the stellarium remote control"),
}


class _MissingExtraFinder:
    @staticmethod
    def find_spec(fullname, path=None, target=None):
        if path is not None or fullname not in OPTIONAL_MODULES:
            return None
        extra, purpose = OPTIONAL_MODULES[fullname]
        raise ModuleNotFoundError(
            f"No module named '{fullname}': libaditya needs it for {purpose}. "
            f"Install it with: pip install 'libaditya[{extra}]'",
            name=fullname,
        )


def install():
    if not any(isinstance(f, _MissingExtraFinder) for f in sys.meta_path):
        sys.meta_path.append(_MissingExtraFinder())
