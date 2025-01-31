# Real-Time Deepfake Detection System

A robust deep learning system for detecting deepfake videos in real-time using Python, OpenCV, and PyTorch. The system combines traditional computer vision techniques with modern deep learning approaches to provide accurate deepfake detection.

## 🌟 Features

- **Real-time Detection**: Process live webcam feed or video files
- **Multiple Face Detection**: Handle multiple faces in a single frame
- **Visual Feedback**: Color-coded boxes and labels for detection results
- **GPU Acceleration**: Utilizes GPU for faster processing when available
- **High Accuracy**: Uses pre-trained models on the VGGFace2 dataset
- **Interactive Interface**: Real-time visualization with confidence scores

## 🛠️ Technologies Used

- Python 3.x
- PyTorch
- OpenCV (cv2)
- facenet-pytorch
- pytorch-grad-cam
- NumPy
- Pillow (PIL)

## 📋 Prerequisites

Before running this project, make sure you have:

```bash
# Required packages
torch
torchvision
opencv-python
facenet-pytorch
pytorch-grad-cam
pillow
numpy
```

## 💻 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/realtime-deepfake-detection.git
cd realtime-deepfake-detection
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Process Video File

```python
python video_detection.py
```

### For Custom Video Input

Modify the video file path in `video_detection.py`:
```python
video_file_path = "path/to/your/video.mp4"
```

## 📁 Project Structure

```
realtime-deepfake-detection/
│
├── face_detection.py       # Face detection module using Haar Cascades
├── deepfake_detection.py   # Core deepfake detection implementation
├── video_detection.py      # Video processing and main execution
├── requirements.txt        # Project dependencies
├── README.md              # Project documentation
│
└── datasets/              # Dataset directory
    ├── real/             # Real video samples
    └── fake/             # Deepfake video samples
```

## 🔧 Components

### 1. Face Detection Module
- Uses Haar Cascade Classifier
- Detects multiple faces in frames
- Returns face coordinates

### 2. Deepfake Detection Module
- Implements MTCNN for face processing
- Uses InceptionResnetV1 for classification
- Includes GradCAM visualization
- Provides confidence scores

### 3. Video Processing Module
- Handles video input/output
- Manages frame processing
- Provides user interface

## 📊 Detection Results

The system provides:
- Visual indicators:
  - Red boxes: Detected deepfakes
  - Blue boxes: Real faces
- Confidence scores in console
- Real-time processing feedback

## 🎯 Performance

- Optimized for real-time processing
- GPU acceleration when available
- Efficient memory usage
- Support for multiple face detection

## 🔍 How It Works

1. **Input Processing**
   - Read video frames
   - Convert color spaces
   - Prepare for detection

2. **Face Detection**
   - Detect faces using Haar Cascades
   - Extract face regions
   - Apply size constraints

3. **Deepfake Analysis**
   - Process through MTCNN
   - Analyze using InceptionResnetV1
   - Generate confidence scores

4. **Output Generation**
   - Draw bounding boxes
   - Display labels
   - Show confidence scores

## 🛑 Limitations

- Requires good lighting conditions
- Face needs to be relatively front-facing
- Performance depends on hardware capabilities
- Minimum face size requirement (40x40 pixels)

## 🔜 Future Improvements

- [ ] Add support for more video formats
- [ ] Implement batch processing
- [ ] Add model fine-tuning options
- [ ] Improve processing speed
- [ ] Add more visualization options
- [ ] Support for different deep learning models

## 🙏 Acknowledgments

- FaceNet PyTorch implementation
- OpenCV community
- PyTorch team
- VGGFace2 dataset creators
