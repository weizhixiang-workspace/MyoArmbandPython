NUMBER_OF_SENSORS = 4
NUMBER_OF_GESTURES = 10

# Sample rate for each sensor
FREQUENCY_EMG = 200
FREQUENCY_ORI = 50
FREQUENCY_ACC = 50
FREQUENCY_GYR = 50

DATA_TIME_INTERVAL_GESTURE = 3 # Gesture interval for recording in seconds

# Data length for each sensor for each record based on time interval and frequence
DATA_LENGTH_EMG = FREQUENCY_EMG * DATA_TIME_INTERVAL_GESTURE
DATA_LENGTH_ORI = FREQUENCY_ORI * DATA_TIME_INTERVAL_GESTURE
DATA_LENGTH_ACC = FREQUENCY_ACC * DATA_TIME_INTERVAL_GESTURE
DATA_LENGTH_GYR = FREQUENCY_GYR * DATA_TIME_INTERVAL_GESTURE

#Number of arrays for each sensor
NUMBER_OF_EMG_ARRAYS = 8
NUMBER_OF_ACC_ARRAYS = 3
NUMBER_OF_GYR_ARRAYS = 3
NUMBER_OF_ORI_ARRAYS = 4

# emg Neural Network Variables
EMG_NN_NUMBER_OF_INPUT = NUMBER_OF_EMG_ARRAYS
EMG_NN_NUMBER_OF_OUTPUT = NUMBER_OF_GESTURES
EMG_NN_NUMBER_OF_LAYERS = 3
EMG_NN_NUMBER_OF_NEURONS_HIDDEN = { NUMBER_OF_EMG_ARRAYS }
EMG_NN_TRAINING_FILENAME = "NNdata/emg.data"
EMG_NN_FILENAME = "NNdata/emg_float.net"

RECORD_PRESTART_MESSEGE = "Press <Enter> to start recording..."

DATA_SET_FOLDER = "data/"
RAW_DATA_FOLDER = "raw_files/"
COMPRESSED_DATA_FOLDER = "compressed_files/"
TEST_SET_FOLDER = "test_set/"
TRAINING_SET_FOLDER = "training_set/"
RECORDED_SET_FOLDER = "recorded_set/"

# Pewter json constants
JSON_ARRAY_DATA_TABLE_NAME = "data"
JSON_EMG_ARRAY_NAME = "emg"
JSON_ORI_ARRAY_NAME = "ori"
JSON_GYR_ARRAY_NAME = "gyr"
JSON_ACC_ARRAY_NAME = "acc"

EMG_INTERVAL_LENGTH = 100
EMG_WAVELET_LEVEL = 1
