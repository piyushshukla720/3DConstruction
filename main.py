import meshroom
import os

photos_path = "/Images"
photos = [os.path.join(photos_path, p) for p in os.listdir(photos_path)]

meshroom_api = meshroom.Meshroom()
meshroom_api.addPhotos(photos)
reconstruction_params = {
    "method": "incremental",
    "depthMapMethod": "photogrammetry",
    "minAngleForStereo": 2.0,
    "minNumberOfMatches": 30,
    "useLocalBA": True
}

meshroom_api.setReconstruction(reconstruction_params)
meshroom_api.start()
output_path = "/Outputs"
meshroom_api.export(output_path)
