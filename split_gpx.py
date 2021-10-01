"""
Split given gpx file into several files of given maximum length.
"""
from argparse import ArgumentParser

import gpxpy

def find_split_index(segment, max_distance):
    """
    Return index of the first point farther than `max_distance`
    """
    i_a, i_b = 0, segment.get_points_no()
    while i_b - i_a > 1:
        # `segment` is joined at this point
        i_mid = i_a + (i_b - i_a) // 2
        s_a, s_b = segment.split(i_mid)
        d_mid = s_a.length_2d()

        s_a.join(s_b)
        if d_mid == max_distance:
            break
        elif d_mid > max_distance:
            i_b = i_mid
        elif d_mid < max_distance:
            i_a = i_mid

    return i_mid

def main(input_file, output_file, max_distance=5e4, max_segments=10):
    """
    input_file : string
    output_file : format string; number of segment is passed
    max_distance : float, in meters; maximum length of the resulting segments
    max_segments : int; max. number of resulting segments; if too low, the last
                   segment will be longer than `max_distance`
    """
    with open(input_file, 'r') as gf:
        gpx = gpxpy.parse(gf)

    for ii in range(max_segments):
        if gpx.tracks[0].segments[-1].length_2d() < max_distance:
            break

        split_index = find_split_index(
            gpx.tracks[0].segments[ii], max_distance)
        gpx.split(0, ii, split_index)

    for ii, seg in enumerate(gpx.tracks[0].segments):
        _gpx = gpxpy.gpx.GPX()
        _trk = gpxpy.gpx.GPXTrack()
        _trk.segments.append(seg)
        _gpx.tracks.append(_trk)
        with open(output_file % ii, 'w') as gf:
            gf.writelines(_gpx.to_xml())

def parse_args():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('INPUT_FILE', help='File name of the input gpx file.')
    parser.add_argument(
        '--output-file', '-o', default='segment_%02d.gpx',
        help='Base name for the output files; default: %(default)s')
    parser.add_argument(
        '--max-segments', default=10,
        help='Maximum number of splits; default: %(default)s')
    parser.add_argument(
        '--max-distance', '-d', default=50.,
        help='Maximum segment distance in km; default: %(default)s')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    main(
        args.INPUT_FILE, args.output_file, max_distance=1e3 * args.max_distance,
        max_segments=args.max_segments
    )
