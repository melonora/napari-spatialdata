from __future__ import annotations

from typing import TYPE_CHECKING

from loguru import logger
from napari import Viewer
from napari.layers import Image, Labels, Points, Shapes
from napari.utils.notifications import show_info

if TYPE_CHECKING:
    from napari.utils.events.event import Event


class SpatialDataViewer:
    def __init__(self) -> None:
        self._viewer = Viewer()
        self._viewer.layers.events.inserted.connect(self._on_add_layer)

    def _on_add_layer(self, event: Event) -> None:
        layer = event.value
        active_layer = self._viewer.layers.selection.active

        if type(layer) in {Labels, Points, Shapes} and "sdata" not in layer.metadata:
            active_layer_metadata = active_layer.metadata
            layer.metadata["sdata"] = active_layer_metadata["sdata"]
            layer.metadata["_current_cs"] = active_layer_metadata["_current_cs"]
            layer.metadata["_active_in_cs"] = {active_layer_metadata["_current_cs"]}
            # For saving with same transformations as parent later. Only image is a valid parent
            if type(active_layer) == Image:
                layer.metadata["_parent_element"] = active_layer.name
            else:
                logger.warning(f"Type of parent layer is not {Image}, but {type(active_layer)} instead")
            show_info(f"The spatialdata object is set to the spatialdata object of {active_layer}")
