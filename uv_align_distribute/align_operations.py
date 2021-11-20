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
from math import radians

import mathutils
from bpy.props import BoolProperty

from . import make_islands, operator_manager, templates, utils

#####################
# ALIGN
#####################

class FillXY(templates.UvOperatorTemplate):
    """Fill whole UV Space"""
    bl_idname = "uv.fill_xy"
    bl_label = "Fill UV space"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        gsettings = context.scene.uv_align_distribute
        makeIslands = make_islands.MakeIslands()
        
        selectedIslands = makeIslands.selectedIslands()
        for island in selectedIslands:
            island.scale(1.0/island.size().width, 1.0/island.size().height)
        
        utils.update()
        return {"FINISHED"}

class AlignSXMargin(templates.UvOperatorTemplate):
    """Align left margin."""

    bl_idname = "uv.align_left_margin"
    bl_label = "Align left margin"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        gsettings = context.scene.uv_align_distribute
        makeIslands = make_islands.MakeIslands()

        selectedIslands = makeIslands.selectedIslands()

        targetElement = None

        if gsettings.relativeItems == "UV_SPACE":
            targetElement = 0.0
        elif gsettings.relativeItems == "ACTIVE":
            activeIsland = makeIslands.activeIsland()
            if activeIsland:
                targetElement = activeIsland.BBox().left()
            else:
                self.report({"ERROR"}, "No active face")
                return {"CANCELLED"}
        elif gsettings.relativeItems == "CURSOR":
            # targetElement = context.space_data.cursor_location.x
            targetElement = utils.getTargetPoint(context, None).x

        if gsettings.selectionAsGroup:
            groupBox = utils.GBBox(selectedIslands)
            if gsettings.relativeItems == "ACTIVE":
                selectedIslands.remove(makeIslands.activeIsland())
            for island in selectedIslands:
                vector = mathutils.Vector((targetElement - groupBox.left(), 0.0))
                island.move(vector)

        else:
            for island in selectedIslands:
                vector = mathutils.Vector((targetElement - island.BBox().left(), 0.0))
                island.move(vector)

        utils.update()
        return {"FINISHED"}


class AlignRxMargin(templates.UvOperatorTemplate):
    """Align right margin."""

    bl_idname = "uv.align_right_margin"
    bl_label = "Align right margin"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        gsettings = context.scene.uv_align_distribute
        makeIslands = make_islands.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()

        targetElement = None

        if gsettings.relativeItems == "UV_SPACE":
            targetElement = 1.0
        elif gsettings.relativeItems == "ACTIVE":
            activeIsland = makeIslands.activeIsland()
            if activeIsland:
                targetElement = activeIsland.BBox().right()
            else:
                self.report({"ERROR"}, "No active face")
                return {"CANCELLED"}
        elif gsettings.relativeItems == "CURSOR":
            # targetElement = context.space_data.cursor_location.x
            targetElement = utils.getTargetPoint(context, None).x

        if gsettings.selectionAsGroup:
            groupBox = utils.GBBox(selectedIslands)
            if gsettings.relativeItems == "ACTIVE":
                selectedIslands.remove(makeIslands.activeIsland())
            for island in selectedIslands:
                vector = mathutils.Vector((targetElement - groupBox.right(), 0.0))
                island.move(vector)

        else:
            for island in selectedIslands:
                vector = mathutils.Vector((targetElement - island.BBox().right(), 0.0))
                island.move(vector)

        utils.update()
        return {"FINISHED"}


##################################################
class AlignTopMargin(templates.UvOperatorTemplate):
    """Align top margin."""

    bl_idname = "uv.align_top_margin"
    bl_label = "Align top margin"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        gsettings = context.scene.uv_align_distribute
        makeIslands = make_islands.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()

        targetElement = None

        if gsettings.relativeItems == "UV_SPACE":
            targetElement = 1.0
        elif gsettings.relativeItems == "ACTIVE":
            activeIsland = makeIslands.activeIsland()
            if activeIsland:
                targetElement = activeIsland.BBox().top()
            else:
                self.report({"ERROR"}, "No active face")
                return {"CANCELLED"}
        elif gsettings.relativeItems == "CURSOR":
            # targetElement = context.space_data.cursor_location.y
            targetElement = utils.getTargetPoint(context, None).y

        if gsettings.selectionAsGroup:
            groupBox = utils.GBBox(selectedIslands)
            if gsettings.relativeItems == "ACTIVE":
                selectedIslands.remove(makeIslands.activeIsland())
            for island in selectedIslands:
                vector = mathutils.Vector((0.0, targetElement - groupBox.top()))
                island.move(vector)

        else:
            for island in selectedIslands:
                vector = mathutils.Vector((0.0, targetElement - island.BBox().top()))
                island.move(vector)

        utils.update()
        return {"FINISHED"}


class AlignLowMargin(templates.UvOperatorTemplate):
    """Align low margin."""

    bl_idname = "uv.align_low_margin"
    bl_label = "Align low margin"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        gsettings = context.scene.uv_align_distribute
        makeIslands = make_islands.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()

        targetElement = None

        if gsettings.relativeItems == "UV_SPACE":
            targetElement = 0.0
        elif gsettings.relativeItems == "ACTIVE":
            activeIsland = makeIslands.activeIsland()
            if activeIsland:
                targetElement = activeIsland.BBox().bottom()
            else:
                self.report({"ERROR"}, "No active face")
                return {"CANCELLED"}
        elif gsettings.relativeItems == "CURSOR":
            # targetElement = context.space_data.cursor_location.y
            targetElement = utils.getTargetPoint(context, None).y

        if gsettings.selectionAsGroup:
            groupBox = utils.GBBox(selectedIslands)
            if gsettings.relativeItems == "ACTIVE":
                selectedIslands.remove(makeIslands.activeIsland())
            for island in selectedIslands:
                vector = mathutils.Vector((0.0, targetElement - groupBox.bottom))
                island.move(vector)

        else:
            for island in selectedIslands:
                vector = mathutils.Vector((0.0, targetElement - island.BBox().bottom()))
                island.move(vector)

        utils.update()
        return {"FINISHED"}


class AlignHAxis(templates.UvOperatorTemplate):
    """Align horizontal axis."""

    bl_idname = "uv.align_horizontal_axis"
    bl_label = "Align horizontal axis"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        gsettings = context.scene.uv_align_distribute
        makeIslands = make_islands.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()

        targetElement = None

        if gsettings.relativeItems == "UV_SPACE":
            targetElement = 0.5
        elif gsettings.relativeItems == "ACTIVE":
            activeIsland = makeIslands.activeIsland()
            if activeIsland:
                targetElement = activeIsland.BBox().center().y
            else:
                self.report({"ERROR"}, "No active face")
                return {"CANCELLED"}
        elif gsettings.relativeItems == "CURSOR":
            # targetElement = context.space_data.cursor_location.y
            targetElement = utils.getTargetPoint(context, None).y

        if gsettings.selectionAsGroup:
            groupBoxCenter = utils.GBBox(selectedIslands).center()
            if gsettings.relativeItems == "ACTIVE":
                selectedIslands.remove(makeIslands.activeIsland())
            for island in selectedIslands:
                vector = mathutils.Vector((0.0, targetElement - groupBoxCenter.y))
                island.move(vector)

        else:
            for island in selectedIslands:
                vector = mathutils.Vector(
                    (0.0, targetElement - island.BBox().center().y)
                )
                island.move(vector)

        utils.update()
        return {"FINISHED"}


class AlignVAxis(templates.UvOperatorTemplate):
    """Align vertical axis."""

    bl_idname = "uv.align_vertical_axis"
    bl_label = "Align vertical axis"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        gsettings = context.scene.uv_align_distribute
        makeIslands = make_islands.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()

        targetElement = None

        if gsettings.relativeItems == "UV_SPACE":
            targetElement = 0.5
        elif gsettings.relativeItems == "ACTIVE":
            activeIsland = makeIslands.activeIsland()
            if activeIsland:
                targetElement = activeIsland.BBox().center().x
            else:
                self.report({"ERROR"}, "No active face")
                return {"CANCELLED"}
        elif gsettings.relativeItems == "CURSOR":
            # targetElement = context.space_data.cursor_location.x
            targetElement = utils.getTargetPoint(context, None).x

        if gsettings.selectionAsGroup:
            groupBoxCenter = utils.GBBox(selectedIslands).center()
            if gsettings.relativeItems == "ACTIVE":
                selectedIslands.remove(makeIslands.activeIsland())
            for island in selectedIslands:
                vector = mathutils.Vector((targetElement - groupBoxCenter.x, 0.0))
                island.move(vector)

        else:
            for island in selectedIslands:
                vector = mathutils.Vector(
                    (targetElement - island.BBox().center().x, 0.0)
                )
                island.move(vector)

        utils.update()
        return {"FINISHED"}


#########################################
class AlignRotation(templates.UvOperatorTemplate):
    """Align island rotation."""

    bl_idname = "uv.align_rotation"
    bl_label = "Align island rotation"
    bl_options = {"REGISTER", "UNDO"}

    method: BoolProperty(
        name="2nd Method",
        description="Second method if normal one doesn't work",
        default=False,
    )

    # wider: BoolProperty(
    #     name="Width",
    #     description="Second method if normal one doesn't work",
    #     default=False,
    # )

    def execute(self, context):
        makeIslands = make_islands.MakeIslands()
        selectedIslands = makeIslands.selectedIslands()
        activeIsland = makeIslands.activeIsland()

        if not activeIsland:
            self.report({"ERROR"}, "No active face")
            return {"CANCELLED"}

        def islandType(island):
            islandSize = island.size()
            if islandSize.width > islandSize.height:
                return "wider"
            else:
                return "higher"

        if self.method:
            activeIslandSize = activeIsland.size()
            selectedIslands.remove(activeIsland)
            activeIslandType = islandType(activeIsland)
            for island in selectedIslands:
                islandSize = island.size()
                if self.method:
                    if islandType(island) != activeIslandType:
                        if activeIslandSize.height > islandSize.height:
                            island.rotate(radians(90))
                        else:  # activeIslandSize.width > islandSize.width:
                            island.rotate(radians(90))
        else:
            activeAngle = activeIsland.angle()
            for island in selectedIslands:
                uvAngle = island.angle()
                deltaAngle = activeAngle - uvAngle
                deltaAngle = round(-deltaAngle, 5)

                island.rotate(deltaAngle)

        utils.update()
        return {"FINISHED"}


#################################
# REGISTRATION
#################################
_om = operator_manager.om
_om.addClass(AlignHAxis)
_om.addClass(AlignVAxis)
_om.addClass(AlignRotation)
_om.addClass(AlignRxMargin)
_om.addClass(AlignSXMargin)
_om.addClass(AlignLowMargin)
_om.addClass(AlignTopMargin)
