# The Dark Knight
## WRO Future Engineers 2026 — Team Current
### v1.0 — Nationals Configuration

This repository contains the current Nationals configuration of **The Dark Knight**, Team Current's WRO Future Engineers 2026 robot.

The purpose of this README is to make the repository easy to audit against the engineering documentation, source code, CAD, schematic and recorded testing evidence.


## Table of Contents

- [1. Team](#1-team)
- [2. Final Robot Overview](#2-final-robot-overview)
- [3. Robot and CAD Visual Reference](#3-robot-and-cad-visual-reference)
  - [Final STL Files](#final-stl-files)
- [4. Final Robot Specifications](#4-final-robot-specifications)
- [5. Mechanical Design](#5-mechanical-design)
- [6. Cameras and Perception](#6-cameras-and-perception)
- [7. Computer Vision](#7-computer-vision)
- [8. Steering](#8-steering)
- [9. Software Architecture](#9-software-architecture)
- [10. Open Challenge](#10-open-challenge)
- [11. Obstacle Challenge](#11-obstacle-challenge)
- [12. Parking and MPU6050](#12-parking-and-mpu6050)
- [13. Power Architecture](#13-power-architecture)
- [14. Measured Power Results](#14-measured-power-results)
- [15. Engineering Evolution](#15-engineering-evolution)
- [16. Recorded Challenge Performance](#16-recorded-challenge-performance)
- [17. Known Development History](#17-known-development-history)
- [18. Repository Structure](#18-repository-structure)
- [19. Reproducibility](#19-reproducibility)
- [20. Evidence Included in This Repository](#20-evidence-included-in-this-repository)
- [21. Final Nationals Configuration Verification](#21-final-nationals-configuration-verification)
- [22. Version](#22-version)

---

> **Consistency rule:** The final engineering document is the reference for the documented physical design and measured results. The Python source in `code/` is the reference for the actual software implementation. If a value is not measured or cannot be confirmed from the supplied material, it is explicitly marked as not measured / not confirmed rather than invented.

---

# 1. Team

| Name | Role |
|---|---|
| **Darsh Makadia** | Programming & Electronics |
| **Ehan Mansuri** | Mechanical Design & 3D Modelling |
| **Sunil Solanki** | Coach |

**Robot:** The Dark Knight  
**Team:** Team Current  
**Competition:** WRO Future Engineers 2026

---

# 2. Final Robot Overview

The Dark Knight is an autonomous four-wheel-drive robot developed for WRO Future Engineers.

The final architecture combines:

- Raspberry Pi 5 (4 GB) as the main computer
- Two Raspberry Pi Camera Module 3 cameras
- JGB37-520 DC motor, 12 V, 600 RPM
- Servo steering
- MPU6050 gyroscope/IMU
- TB6612FNG motor driver
- 3S 2200 mAh LiPo battery
- CAD/PLA structural parts
- LEGO drivetrain components
- A mechanical LEGO differential
- A central driveshaft transmitting drive through the drivetrain

The project evolved through physical testing rather than being designed completely on paper. Major iterations involved the drivetrain, chassis, camera arrangement, power distribution, computer vision, navigation, obstacle avoidance and parking.

---



---

# 3. Robot and CAD Visual Reference

The visual assets below are stored in the repository using the same vehicle-photo convention as the original GitHub README: `v-photos/`. CAD preview images are in `models/`, and the final schematic preview is in `schemes/`.

## Robot Photos

### Front View

<img src="./v-photos/front_view.png" alt="The Dark Knight front view" width="600">

### Back View

<img src="./v-photos/back_view.png" alt="The Dark Knight back view" width="600">

### Side Views

<p align="center">
  <img src="./v-photos/side_view_1.png" alt="The Dark Knight side view 1" width="45%">
  <img src="./v-photos/side_view_2.png" alt="The Dark Knight side view 2" width="45%">
</p>

### Motor and Steering

<p align="center">
  <img src="./v-photos/motor_close_up.png" alt="JGB37-520 drive motor" width="45%">
  <img src="./v-photos/servo_close_up.png" alt="Steering servo" width="45%">
</p>

### Differential and Electronics

<p align="center">
  <img src="./v-photos/differential.png" alt="Mechanical LEGO differential" width="45%">
  <img src="./v-photos/circuit_case_and_battery.png" alt="Electronics and battery" width="45%">
</p>

### Electronics From Above

<p align="center">
  <img src="./v-photos/circuit_from_top.png" alt="Electronics from top" width="700">
</p>

## CAD Models

### Final Chassis

<img src="./models/chassis.png" alt="Final CAD chassis" width="700">

### Circuit Box

<img src="./models/circuit_box.png" alt="Circuit box CAD" width="700">

### Circuit Box Lid

<img src="./models/circuit_box_lid.png" alt="Circuit box lid CAD" width="700">

### Camera Mount

<img src="./models/camera_mount.png" alt="Dual-camera mounting component" width="700">

### Camera Case

<img src="./models/camera_case.png" alt="Camera case CAD" width="600">

## Circuit Schematic

<img src="./schemes/schematic.png" alt="Final circuit schematic" width="1000">


## Final STL Files

The final CAD source files supplied for the Nationals configuration are stored in [`cad/`](./cad/). The STL files are included as downloadable manufacturing files rather than embedded directly in the README, because GitHub does not reliably render STL geometry inline inside a Markdown page.

### Final supplied STL models

| Model | STL file | Purpose |
|---|---|---|
| Final chassis | [`currents final chassis.stl`](./cad/currents%20final%20chassis.stl) | Main custom chassis |
| Final chassis — Part 2 | [`currents final chassis pt2.stl`](./cad/currents%20final%20chassis%20pt2.stl) | Additional chassis component |
| Dual-camera mount | [`currnts dual camera mount.stl`](./cad/currnts%20dual%20camera%20mount.stl) | Camera mounting component |
| Camera case | [`camera case (1).stl`](./cad/camera%20case%20%281%29.stl) | Camera protection/enclosure |
| Circuit box | [`currents CB.stl`](./cad/currents%20CB.stl) | Electronics enclosure |
| Circuit box lid | [`currents CB LID.stl`](./cad/currents%20CB%20LID.stl) | Electronics enclosure lid |

These are the STL files supplied by the team for the final repository package. The corresponding CAD preview images remain in [`models/`](./models/) and the STL files themselves remain in [`cad/`](./cad/).

# 4. Final Robot Specifications

| Specification | Final documented value |
|---|---:|
| Length | **24 cm** |
| Width | **13 cm** |
| Height | **27.5 cm** |
| Mass | **863 g** |
| Wheel diameter | **43.2 mm** |
| Gear ratio | **1.8:1** |
| Drive configuration | **Four-wheel drive** |
| Differential | **Mechanical LEGO differential** |
| Drive motor | **JGB37-520 DC 12 V, 600 RPM** |
| Steering | **Servo steering** |
| Main computer | **Raspberry Pi 5, 4 GB** |
| Vision | **Two cameras + OpenCV** |
| Orientation | **MPU6050** |
| Structural material | **PLA / CAD printed parts** |

The final documentation explains that the drivetrain changed to four-wheel drive because large steering angles during parking could otherwise increase wheel slip and reduce control. The mechanical differential was retained because it provided a compact mechanical solution without requiring a custom manufactured differential.

---

# 5. Mechanical Design

## 4.1 CAD + LEGO hybrid architecture

The robot is not an all-LEGO chassis and it is not an all-CAD drivetrain.

The final design deliberately combines:

**CAD/PLA**
- structural chassis
- electronics/circuit enclosure
- camera mounting geometry
- camera protection
- other custom mounting components

**LEGO Technic**
- drivetrain components
- mechanical differential
- gears
- shafts/connectors
- steering/mechanical linkage components

This approach reduced unnecessary manufacturing complexity while allowing the team to make the structural geometry fit the electronics and drivetrain.

## 4.2 Four-wheel drive

The final robot uses **4WD**.

Power from the drive motor is transmitted through a central driveshaft and the front/rear drivetrain mechanisms. The mechanical differentials allow the left and right wheels to rotate at different speeds during turns.

The final engineering document specifically describes the 4WD decision as a response to the sharp steering required during parking.

## 4.3 Gear ratio

The final documented gear ratio is:

**1.8:1**

The development process traded some available torque for higher wheel speed because the earlier torque capacity was more than required for the robot's operating conditions.

The final documented speed test was:

| Test | Result |
|---|---:|
| Distance | **3 m** |
| Time | **2.25 s** |
| Measured speed | **1.33 m/s** |
| Equivalent | **4.8 km/h** |

---

# 6. Cameras and Perception

The final robot uses **two Raspberry Pi Camera Module 3 cameras**.

## Front camera

Primary role:

- track/line perception
- blue/orange direction markers
- red obstacles
- green obstacles

Documented setup:

- **1480 × 520**
- target **60 FPS**
- lens-centre height approximately **25.0 cm**

## Rear / parking camera

Primary role:

- rearward parking-area/marker perception
- parking sequence support

Documented setup:

- **640 × 480**
- target **60 FPS**
- lens-centre height approximately **23.5 cm**

The two-camera arrangement was selected so the robot could maintain forward perception while also obtaining information behind the robot during parking.

---

# 7. Computer Vision

The software uses **OpenCV** and both **HSV and LAB** colour representations.

The documented obstacle/colour confidence model is:

**Confidence = 0.65 × HSV + 0.20 × LAB + 0.15 × geometry**

The current `vision.py` implementation:

1. creates colour masks;
2. performs morphological cleaning;
3. extracts contours;
4. rejects detections below the configured minimum area;
5. evaluates HSV coverage;
6. evaluates LAB colour similarity;
7. evaluates contour geometry;
8. combines the scores into a confidence value;
9. selects a target using confidence, area and position weighting.

This is more selective than simply taking the largest coloured contour.

### Detection classes

The repository contains processing for:

- black track boundaries
- blue markers
- orange markers
- green obstacles
- red obstacles
- magenta parking structures/markers

The exact colour thresholds are calibration values in `code/vision.py`. They should be changed only after physical re-testing.

---

# 8. Steering

The actual software configuration in `code/config.py` and `code/drive.py` uses:

| Setting | Value |
|---|---:|
| Servo centre | **75°** |
| Minimum | **35°** |
| Maximum | **115°** |

The drive layer clamps every requested steering angle to this range.

**35° ≤ steering ≤ 115°**

These are the final documented/calibrated values. Older repository descriptions using values such as 70°, 95–98° or 125–130° are development-era values and should not be used as the Nationals configuration.

---

# 9. Software Architecture

The software runs in Python on the Raspberry Pi 5.

Main modules:

| File | Purpose |
|---|---|
| `config.py` | Central calibration/configuration |
| `drive.py` | Motor and steering control |
| `heading.py` | MPU6050 gyro heading and calibration |
| `vision.py` | Camera and colour/target processing |
| `openVision.py` | Open Challenge vision compatibility |
| `open_challenge.py` | Open Challenge navigation |
| `obstacle_challenge.py` | Obstacle detection/avoidance |
| `parking.py` | Direction-dependent parking state machine |
| `run_open.py` | Open Challenge launcher |
| `run_obstacle.py` | Obstacle Challenge launcher |

Important safety behaviour in the current source includes:

- steering saturation
- temporal confirmation for obstacle detections
- I2C/IMU error handling
- bounded IMU turning loops
- safe-stop behaviour
- cleanup without starting a new manoeuvre from `finally`

---

# 10. Open Challenge

## 9.1 Navigation

The final documented navigation approach uses direction-dependent wall following:

- **Clockwise → right wall**
- **Anticlockwise → left wall**

The team moved away from relying on the centre between two walls because losing one wall could produce an unstable centre estimate.

## 9.2 Direction markers

The software uses:

- **Blue → anticlockwise**
- **Orange → clockwise**

## 9.3 Marker counting

The final documented Open Challenge configuration is:

| Parameter | Value |
|---|---:|
| `KP` | **0.013** |
| Laps | **3** |
| Relevant crossings/lap | **4** |
| Total counted crossings | **12** |
| Marker cooldown | **1.0 s** |
| Servo centre | **75°** |
| Servo limits | **35°–115°** |
| Initial motor PWM | **40** |

The marker counter uses rising-edge logic so that one physical marker crossing is not counted repeatedly while the marker remains visible.

Conceptually:

```text
not detected → detected = count once
detected → detected = no new count
detected → disappears = ready for next crossing
```

A 1.0-second cooldown is also applied.

## 9.4 Recorded results

The six recorded Open Challenge runs were:

**32, 30, 28, 28, 28, 28 seconds**

**Best recorded time: 28 seconds**

The final engineering document correctly treats these as the team's recorded test results rather than claiming that 28 seconds is a statistically guaranteed performance.

---

# 11. Obstacle Challenge

The obstacle controller gives obstacle detections priority over normal wall following.

The documented high-level hierarchy is:

1. Green obstacle
2. Red obstacle
3. Both useful boundaries
4. Left boundary
5. Right boundary
6. Conservative fallback

Green and red obstacle detections are temporally confirmed in the current source so a single noisy frame does not immediately trigger avoidance.

Obstacle steering is direction-dependent because the same image position does not necessarily require the same manoeuvre in clockwise and anticlockwise travel.

## Parking-marker sequence

The final documentation describes the magenta/purple parking marker as the lap/parking trigger:

- the rear camera detects the marker;
- the marker is passed once per lap;
- the third detection starts the transition toward parking;
- the robot then follows the documented direction-dependent parking approach.

Parking is **not listed as a future/unimplemented feature**. The final document states that the current rear-camera, state-based and IMU-heading approach works reliably in the team's tested configuration.

---

# 12. Parking and MPU6050

Parking uses the **rear camera + explicit state logic + MPU6050 heading feedback**.

## Why the IMU was added

Timed turns do not directly measure orientation. The achieved turn can change with battery condition, motor speed, friction, wheel contact, steering geometry and acceleration.

The final system therefore uses gyro feedback for parking turns.

## MPU6050 calibration

The documented implementation:

- waits for an initial settling period;
- collects **1500 stationary Z-axis gyro samples**;
- averages them to estimate the Z-axis bias;
- subtracts the bias from subsequent readings;
- integrates corrected angular velocity;
- maintains heading in the 0–360° range.

The current source also includes I2C failure handling and bounded turn loops.

## Parking status

**Parking is implemented and tested.**

It should not be described anywhere in the Nationals repository as merely "planned".

---

# 13. Power Architecture

The final system uses a **3S 2200 mAh LiPo** with separate regulated branches.

### Raw battery branch

The battery supplies:

- motor-driver motor voltage
- Buck 1 input
- Buck 2 input

### Buck 1

Regulated 5 V branch used for the servo and motor-driver logic connections documented by the project.

### Buck 2

Regulated 5 V branch used for the Raspberry Pi 5 and its connected peripherals.

### Raspberry Pi 3.3 V

Used for the documented OLED, push-button supply and MPU6050 connections.

### Ground

All branches share a common ground.

---

# 14. Measured Power Results

Only physically documented voltage measurements are included here.

| Point | Condition | Measured |
|---|---|---:|
| LiPo | Before run | **11.1 V** |
| LiPo | After multiple runs | **10.8 V** |
| Buck 1 | Motors OFF | **5.0 V** |
| Buck 1 | Robot moving | **5.0 V** |
| Pi supply | Idle | **5.0 V** |
| Pi supply | Moving | **5.0 V** |
| Motor driver | Motors OFF | **11.1 V** |
| Motor driver | Motors ON | **10.8 V** |

**Current was not measured** with the available setup.

No current values are fabricated in this repository.

The final documentation also notes that these multimeter measurements do not characterise every fast transient or current spike.

---

# 15. Engineering Evolution

The project followed a repeated:

**Problem → Constraint → Decision → Implementation → Test → Observation → Next iteration**

process.

| Problem | Change | Testing / result |
|---|---|---|
| Drivetrain behaviour | Moved toward a speed-oriented final gear configuration | 3 m test: 2.25 s / 1.33 m/s |
| Need for controlled sharp turns | Finalised 4WD with mechanical differential | Better traction/control concept for parking |
| Structural integration | Added CAD/PLA structural components | Custom chassis and mounting geometry |
| Camera perception | Tested camera placement and angle | Final two-camera architecture |
| Power reliability | Separated regulated power branches | Measured 5 V rails remained at 5.0 V in recorded checks |
| Two-wall navigation | Changed to direction-based single-wall following | More reliable when one wall temporarily disappeared |
| Obstacle avoidance | Added target-centering and direction-dependent logic | Improved behaviour around difficult obstacle/corner situations |
| Marker duplicate counting | Rising-edge + cooldown logic | Prevents repeated counts from one physical marker |
| Parking turns | Moved from purely timed turns toward IMU feedback | Current parking sequence works in tested configuration |
| Servo safety | Software steering saturation | Prevents commands beyond tested range |

---

# 16. Recorded Challenge Performance

## Open Challenge

| Run | Time |
|---:|---:|
| 1 | 32 s |
| 2 | 30 s |
| 3 | 28 s |
| 4 | 28 s |
| 5 | 28 s |
| 6 | 28 s |

**Best: 28 s**

## Obstacle Challenge

| Run | Time |
|---:|---:|
| 1 | 1:10 |
| 2 | 1:09 |
| 3 | 1:11 |
| 4 | 1:20 |
| 5 | 1:15 |
| 6 | 1:13 |

**Best: 1:09**

The obstacle runs were not identical trials because obstacle placement varied slightly between runs. The results are therefore preserved exactly as recorded.

---

# 17. Known Development History

Some values appearing in older repository files are development/prototype information, not the final Nationals configuration.

Examples include:

- earlier RWD descriptions;
- earlier single-camera descriptions;
- older steering values;
- older parking-planned wording;
- earlier power-test tables with `TBD` values.

For the Nationals repository, the final architecture is:

**4WD + mechanical LEGO differential + central driveshaft + two cameras + MPU6050 + CAD/PLA chassis + JGB37-520 + TB6612FNG + 3S LiPo.**

The older prototype information should not be presented as the final configuration.

---

# 18. Repository Structure

```text
Team_Currents_Nationals_v1.0/
│
├── README.md
├── VERSION
├── CHANGELOG.md
├── COMMIT_PLAN.md
│
├── code/
│   ├── config.py
│   ├── drive.py
│   ├── heading.py
│   ├── vision.py
│   ├── openVision.py
│   ├── open_challenge.py
│   ├── obstacle_challenge.py
│   ├── parking.py
│   ├── run_open.py
│   └── run_obstacle.py
│
├── cad/
│   ├── final STL exports
│   └── CAD reference images
│
├── models/
│   └── README-compatible CAD preview images
│
├── schematics/
│   └── final schematic reference
│
├── schemes/
│   └── README-compatible schematic preview
│
├── photos/
│   └── source robot/development photographs
│
├── v-photos/
│   └── README-compatible vehicle photographs
│
├── testing/
│   ├── Open_Challenge.mp4
│   ├── test_results.csv
│   ├── power_measurements.csv
│   ├── test_summary.md
│   └── engineering_evolution.md
│
└── documentation/
    └── Team_Currents_Final_Document.pdf
```

The repository structure is intentionally separated into code, CAD, schematics, photos, testing and documentation so that each part of the engineering process can be checked independently.

---

# 19. Reproducibility

A person reproducing the documented system would need, at minimum:

- Raspberry Pi 5, 4 GB
- two Raspberry Pi Camera Module 3 cameras
- JGB37-520 12 V 600 RPM motor
- servo motor
- MPU6050
- TB6612FNG
- 3S 2200 mAh LiPo
- buck converter(s)
- PLA
- required LEGO drivetrain/differential components

Software dependencies documented for the project include:

- Python
- OpenCV
- NumPy
- RPi.GPIO
- Picamera2
- smbus2 for the MPU6050 I2C interface

The exact source implementation is in `code/`.

---

# 20. Evidence Included in This Repository

The current package includes:

- final engineering PDF;
- final Python source;
- supplied final STL exports;
- CAD reference images;
- schematic reference;
- Open Challenge test video;
- recorded challenge results;
- measured power-voltage results;
- engineering evolution notes.

Native editable CAD/schematic source files should only be added if the team actually has those files. They should not be fabricated from screenshots or STL exports.

---

# 21. Final Nationals Configuration Verification

The repository-side consistency check has been completed against the final engineering document, the supplied testing evidence, and the current source tree. This section records the completed state rather than a list of unfinished tasks.

### Configuration verified

| Check | Final status | Source of verification |
|---|---|---|
| Robot drivetrain | **Verified — 4WD** | Final engineering document + repository documentation |
| Differential | **Verified — mechanical LEGO differential with central driveshaft** | Final engineering document |
| Cameras | **Verified — 2 Raspberry Pi Camera Module 3 cameras** | Final engineering document + CAD/test evidence |
| Orientation sensor | **Verified — MPU6050** | Final engineering document + `code/heading.py` |
| Steering | **Verified — 35° minimum / 75° centre / 115° maximum** | `code/config.py` + final document |
| Open Challenge | **Verified — 3 laps / 4 crossings per lap / 12 total / 1.0 s cooldown** | `code/config.py` + final document |
| Direction markers | **Verified — blue anticlockwise / orange clockwise** | Final engineering document + challenge logic |
| Obstacle marker | **Verified — rear-camera magenta/purple marker** | Final engineering document + obstacle code |
| Parking | **Verified — implemented and tested** | Rear camera + state machine + MPU6050 heading feedback |
| Power voltage data | **Verified — only documented measured values included** | `testing/power_measurements.csv` + final document |
| Current data | **Verified — Not measured** | No current-logging measurement was available |
| Challenge results | **Verified — Open best 28 s; Obstacle best 1:09** | `testing/test_results.csv` + final document |
| Repository structure | **Verified** | `code/`, `cad/`, `schematics/`, `photos/`, `testing/`, `documentation/` |
| Final engineering PDF | **Included** | `documentation/Team_Currents_Final_Document.pdf` |
| Supplied STL CAD exports | **Included** | `cad/` |
| Open Challenge video | **Included** | `testing/Open_Challenge.mp4` |

### Final consistency rule

The Nationals repository is now treated as a single configuration. The code, hardware description, CAD references, schematic, testing evidence and engineering PDF must describe the same robot. Older prototype values are retained only where they are explicitly labelled as development history; they are not presented as the final configuration.

### Data-integrity rule

No unmeasured current value has been added. No missing native CAD or schematic source file has been fabricated from an image or STL export. If a future physical change is made to the robot, the corresponding code and documentation must be updated before that change is treated as part of the Nationals configuration.

---

# 22. Version

**v1.0 — Nationals Configuration**

This version is intended to be the clean baseline for Nationals submission and further physical testing.

Recommended commit names:

- `Fix parking state machine`
- `Update obstacle avoidance`
- `Add final testing results`
- `Update final drivetrain`
- `Add power measurements`
- `Update two-camera architecture`
- `v1.0 – Nationals Configuration`

---

## Final Engineering Principle

The goal of this repository is not to make the robot look more advanced than it is.

It is to make the **code, hardware, CAD, testing evidence and engineering documentation tell the same story**.

If something was not measured, it is not presented as measured. If something was only a prototype, it is not presented as the final configuration. If a value changes in the physical robot, the code and documentation should be updated together.
