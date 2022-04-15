# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; version 2
#  of the License.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# Globals:
import bpy
from bpy.props import BoolProperty, EnumProperty

from . import operator_manager
import re


class GlobalSettings(bpy.types.PropertyGroup):
    """UVAlignDistribute globla settings"""

    relativeItems: EnumProperty(
        items=[
            ("UV_SPACE", "Uv Space", "Align to UV space"),
            ("ACTIVE", "Active Face", "Align to active face\\island"),
            ("CURSOR", "Cursor", "Align to cursor"),
        ],
        name="Relative to",
    )

    selectionAsGroup: BoolProperty(
        name="Selection as group", description="Treat selection as group", default=False
    )


bm = None
uvlayer = None

preview_collections = {}
_bversion_string = bpy.app.version_string
_bversion_reg = re.match(r"^(\d\.\d?\d)", _bversion_string)
bversion = float(_bversion_reg.group(0))
operator_manager.om.addClass(GlobalSettings)
