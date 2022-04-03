from napari_spatial_anndata._reader import napari_get_reader
from napari_spatial_anndata._widget import ExampleQWidget, example_magic_widget
from napari_spatial_anndata._writer import write_multiple, write_single_image
from napari_spatial_anndata.interactive import Interactive
from napari_spatial_anndata._sample_data import make_sample_data

__version__ = "0.0.0"

try:
    from importlib_metadata import version  # Python < 3.8
except ImportError:
    from importlib.metadata import version  # Python = 3.8

from packaging.version import parse

try:
    __full_version__ = parse(version(__name__))
    __full_version__ = f"{__version__}+{__full_version__.local}" if __full_version__.local else __version__
except ImportError:
    __full_version__ = __version__

del version, parse