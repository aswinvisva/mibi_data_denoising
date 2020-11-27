from utils import tiff_reader
from utils.mibi_reader import get_all_point_data
from utils.extract_vessel_contours import *
from utils.markers_feature_gen import *
from utils.visualizer import vessel_nonvessel_heatmap, point_region_plots, vessel_region_plots, brain_region_plots, \
    all_points_plots, brain_region_expansion_heatmap, marker_expression_masks, vessel_areas_histogram, \
    pixel_expansion_ring_plots, removed_vessel_expression_boxplot, biaxial_scatter_plot, obtain_expanded_vessel_masks, \
    obtain_embedded_vessel_masks, spatial_probability_maps, expression_histogram, violin_plot_brain_expansion
import config.config_settings as config

'''
Authors: Aswin Visva, John-Paul Oliveria, Ph.D
'''


def run_denoise():
    """
    Create the visualizations for inward and outward vessel expansions and populate all results in the directory
    set in the configuration settings.
    """
    for directory, subdirlist, filelist in os.walk(config.data_dir):
        for f in filelist:
            img = tiff_reader.read(os.path.join(directory, f), describe=True)


if __name__ == '__main__':
    run_denoise()
