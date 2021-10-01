# split_gpx
Split given gpx file into several files of given maximum length.

```
$ python split_gpx.py -h
usage: split_gpx.py [-h] [--output-file OUTPUT_FILE]
                    [--max-segments MAX_SEGMENTS]
                    [--max-distance MAX_DISTANCE]
                    INPUT_FILE

Split given gpx file into several files of given maximum length.

positional arguments:
  INPUT_FILE            File name of the input gpx file.

optional arguments:
  -h, --help            show this help message and exit
  --output-file OUTPUT_FILE, -o OUTPUT_FILE
                        Base name for the output files; default:
                        segment_%02d.gpx
  --max-segments MAX_SEGMENTS
                        Maximum number of splits; default: 10
  --max-distance MAX_DISTANCE, -d MAX_DISTANCE
                        Maximum segment distance in km; default:
                        50.0
```
