---
title: Stereo and 3D
description: Stereo depth video, motion HUD and stereo-inertial odometry (OpenVINS) from Trinet Stereo and Stereo GS recordings.
---

# Stereo and 3D

Stereo takes (`take0002_L.mp4` + `take0002_R.mp4`) are self-contained: frame pairing, motion data
and the camera's factory calibration are read from the files themselves.

## Depth video

```bash
python3 scripts/stereo_depth_video.py captures/take0002 out_depth.mp4 --wls --imu --ema 0.5
```

Renders the rectified left and right images with a metric depth map (semi-global block matching;
`--wls` smoothing needs `opencv-contrib-python`), optionally with a motion strip.

## Motion HUD

```bash
python3 scripts/stereo_motion_hud.py captures/take0002 out_hud.mp4 --start-s 10 --end-s 25
```

Side-by-side playback with a reference grid, live rotation rates and the predicted rolling-shutter
shear for each frame — useful for judging motion blur and skew (and for seeing why Stereo GS avoids
it).

## Stereo-inertial odometry (OpenVINS)

```bash
docker build -t trinet-openvins:latest scripts/openvins-docker/
python3 scripts/make_openvins_config.py captures/take0002_L.mp4 WORK/ov_config
./scripts/run_openvins.sh WORK
python3 scripts/plot_trajectory.py WORK/ov_out/traj_est.txt
```

`make_openvins_config.py` turns the recording's embedded calibration into the configuration files
OpenVINS expects, so a recording carries everything a VIO run needs. See the script's help for
preparing the input bag.

## More

The repository also contains experimental scripts for learned stereo depth, map fusion and Gaussian
splatting (`stereo_depth_neural.py`, `stereo_map_fusion.py`, `gs_*.py`). Run any script with `--help`
for its options.

For your own pipelines, the [reference calibrations](../calibration/reference-calibrations.md) and
their Kalibr export work with VINS-Fusion, Basalt and similar tools.
