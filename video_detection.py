# import cv2
# from face_detection import detect_bounding_box
# from deepfake_detection import predict

# def main():
#     # Open the video file
#     video_capture = cv2.VideoCapture(0)

#     # Check if the video file was opened correctly
#     if not video_capture.isOpened():
#         print("Error: Could not open video file.")
#         return

#     while True:
#         result, video_frame = video_capture.read()
#         if not result:
#             print("Error: Failed to read video frame.")
#             break
        
#         # Perform face detection and deepfake prediction
#         faces = detect_bounding_box(video_frame)
#         video_frame = predict(video_frame)
        
#         # Resize the frame to a smaller size for better display (e.g., 640x480)
        
        
      
        
#         # Display the processed frame
#         cv2.imshow("Deepfake Detection", video_frame)

#         # Press 'q' to quit
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break

#     video_capture.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     # video_file_path = r"C:\Users\KIIT\Downloads\AP LAB\Realtime-Deepfake-Detection-main\datasets\01_02__meeting_serious__YVGY8LOK.mp4"
#     main()  # Start the video processing




import cv2
from face_detection import detect_bounding_box
from deepfake_detection import predict

def main(video_file_path):
    video_capture = cv2.VideoCapture(video_file_path)
    while True:
        result, video_frame = video_capture.read()
        if result is False:
            break
        
        faces = detect_bounding_box(video_frame)
        video_frame = predict(video_frame)

        cv2.imshow("My Face Detection Project", video_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
     video_file_path = r"C:\Users\KIIT\Downloads\AP LAB\Realtime-Deepfake-Detection-main\datasets\real\real_1.mp4"

     main(video_file_path)

