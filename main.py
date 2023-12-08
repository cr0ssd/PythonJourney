from cscore import CameraServer
from ntcore import NetworkTableInstance, EventFlags

import cv2
import json
import numpy as np
import time

import robotpy_apriltag
from wpimath.geometry import Transform3d
import math

team = 5887
server = False


def main():
    with open('/boot/frc.json') as f:
        config = json.load(f)
    camera = config['cameras'][0]

    width = camera['width']
    height = camera['height']

    CameraServer.startAutomaticCapture()

    input_stream = CameraServer.getVideo()
    output_stream = CameraServer.putVideo('Processed', width, height)
    img = np.zeros(shape=(height, width, 3), dtype=np.uint8)

    """ input_stream1 = CameraServer.getVideo()
    output_stream1 = CameraServer.putVideo('Processed', width, height)
    img1 = np.zeros(shape=(height, width, 3), dtype=np.uint8)
    ACTUALIZAR A LOS NUEVOS TAGS PARA LA SIGUIENTE SEASON
"""

    # start NetworkTables
    ntinst = NetworkTableInstance.getDefault()
    print("SERVER?: ", server)
    if server:
        print("Setting up NetworkTables server")
        ntinst.startServer()
    else:
        print("Setting up NetworkTables client for team {}".format(team))
        ntinst.startClient4("wpilibpi")
        ntinst.setServerTeam(team)
        ntinst.startDSClient()

    # Table for vision output information
    vision_nt = ntinst.getTable('Vision')

    # Wait for NetworkTables to start / Intentar abrirlos antes para que no pase lo de mty 
    time.sleep(0.5)

    prev_time = time.time()
    while True:
        start_time = time.time()

        frame_time, input_img = input_stream.grabFrame(img)
        output_img = np.copy(input_img)

        # Coordinates of found targets, for NT output:
        x_list = []
        y_list = []
        id_list = []
        prueba = [0, 1, 30]

        # Notify output of error and skip iteration
        if frame_time == 0:
            output_stream.notifyError(input_stream.getError())
            continue
        # """
        # April Tag detection:
        detector = robotpy_apriltag.AprilTagDetector()
        detector.addFamily("tag16h5")
        # detector.addFamily("tag36h11")
        estimator = robotpy_apriltag.AprilTagPoseEstimator(
            robotpy_apriltag.AprilTagPoseEstimator.Config(
                0.2, 500, 500, width / 2.0, height / 2.0
            )
        )

        # Detect apriltag
        DETECTION_MARGIN_THRESHOLD = 100
        DETECTION_ITERATIONS = 50

        gray = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
        tag_info = detector.detect(gray)
        filter_tags = [tag for tag in tag_info if tag.getDecisionMargin() > DETECTION_MARGIN_THRESHOLD]

        # OPTIONAL: Ignore any tags not in the set used on the 2023 FRC field:
        # filter_tags = [tag for tag in filter_tags if ((tag.getId() > 0) & (tag.getId() < 9))]

        for tag in filter_tags:

            est = estimator.estimateOrthogonalIteration(tag, DETECTION_ITERATIONS)
            pose = est.pose1

            tag_id = tag.getId()
            center = tag.getCenter()
            # hamming = tag.getHamming()
            # decision_margin = tag.getDecisionMargin()
            print(f"{tag_id}: {pose}")

            # Highlight the edges of all recognized tags and label them with their IDs:

            if ((tag_id > 0) & (tag_id < 9)):
                col_box = (0, 255, 0)
                col_txt = (255, 255, 255)
                if tags[4].getId() == 4:
                    print("elevador")
            else:
                col_box = (0, 0, 255)
                col_txt = (0, 255, 255)

            # Draw a frame around the tag:
            corner0 = (int(tag.getCorner(0).x), int(tag.getCorner(0).y))
            corner1 = (int(tag.getCorner(1).x), int(tag.getCorner(1).y))
            corner2 = (int(tag.getCorner(2).x), int(tag.getCorner(2).y))
            corner3 = (int(tag.getCorner(3).x), int(tag.getCorner(3).y))
            cv2.line(output_img, corner0, corner1, color=col_box, thickness=2)
            cv2.line(output_img, corner1, corner2, color=col_box, thickness=2)
            cv2.line(output_img, corner2, corner3, color=col_box, thickness=2)
            cv2.line(output_img, corner3, corner0, color=col_box, thickness=2)

            # Label the tag with the ID:
            cv2.putText(output_img, f"{tag_id}", (int(center.x), int(center.y)), cv2.FONT_HERSHEY_SIMPLEX, 1, col_txt,
                        2)

            x_list.append((center.x - width / 2) / (width / 2))
            y_list.append((center.y - width / 2) / (width / 2))
            id_list.append(tag_id)

        vision_nt.putNumberArray('target_x', x_list)
        vision_nt.putNumberArray('target_y', y_list)
        vision_nt.putNumberArray('target_id', id_list)

        vision_nt.putNumberArray('prueba', prueba)

        # """

        # print(vision_nt.getNumberArray('target_x', x_list))

        processing_time = start_time - prev_time
        prev_time = start_time

        fps = 1 / processing_time
        cv2.putText(output_img, str(round(fps, 1)), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
        output_stream.putFrame(output_img)

        # brithness = ntinst.getTable('camera').getEntry("brightness").getNumber('Brigtness', 0)
        # print(brithness)

        number = 20.0

        # ntinst.getTable('Datos prueba').getEntry('Prueba1').putNumber('prueba', number)

        print("99999999999")


main()


#Para limelight
"""area_max:100
area_min:0.0017850625000000004
area_similarity:0
aspect_max:20.000000
aspect_min:0.000000
black_level:0
blue_balance:1975
botfloorsnap:0
botlength:0.7112
botwidth:0.7112
calibration_type:0
classifier_conf:0.100000
contour_grouping:0
contour_sort_final:0
convexity_max:100
convexity_min:10
corner_approx:5.000000
crop_x_max:1.000000
crop_x_min:-1.000000
crop_y_max:1.000000
crop_y_min:-1.000000
cross_a_a:1
cross_a_x:0
cross_a_y:0
cross_b_a:1
cross_b_x:0
cross_b_y:0
desc:Pipeline_Name
desired_contour_region:0
detector_conf:0.800000
dilation_steps:0
direction_filter:0
dual_close_sort_origin:0
erosion_steps:0
exposure:131
fiducial_decoder_strictness:strict
fiducial_denoise:0.000000
fiducial_idfilters:
fiducial_locfilters:
fiducial_resdiv:4
fiducial_size:152.4
fiducial_skip3d:0
fiducial_type:aprilClassic16h5
fiducial_vis_mode:3dbotposetargspace
force_convex:1
hue_max:85
hue_min:60
image_flip:0
image_source:0
img_to_show:0
intersection_filter:0
invert_hue:0
lcgain:20
multigroup_max:7
multigroup_min:1
multigroup_rejector:0
pipeline_led_enabled:0
pipeline_led_power:100
pipeline_res:3
pipeline_type:3
red_balance:1200
roi_x:0.000000
roi_y:0.000000
rsf:0.0508
rspitch:-20
rsroll:0.000000
rss:0.000000
rsu:0.854075
rsyaw:0.000000
sat_max:255
sat_min:70
send_corners:0
send_raw_contours:0
solve3d:0
solve3d_algo:0
solve3d_bindtarget:1
solve3d_conf:0.990000
solve3d_error:8
solve3d_guess:0
solve3d_iterations:50
solve3d_precise:0
solve3d_zoffset:0.000000
tsf:0
tss:0
tsu:0
val_max:255
val_min:70
x_outlier_miqr:1.5
y_outlier_miqr:1.5 """