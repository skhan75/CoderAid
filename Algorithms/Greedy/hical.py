""" INTERVIEW CAKE
Your company built an in-house calendar tool called HiCal.
You want to add a feature to see the times in a day when everyone is available.

To do this, you'll ned to know when any team is having a meeting
In HiCal, a meeting is stored as a tuple of integers (start_time, end_time).
These integers represent the number of 30-minute blocks past 9:00am.
"""



import unittest


def merge_ranges(meetings):

    # Sort the list of tuples by Start time
    meetings = sorted(meetings)

    # Append first meeting of the day as our first meeting
    merged_meetings = [meetings[0]]

    for current_start, current_finish in meetings[1:]:

        # Get the last merged meeting start and finish times
        last_merged_meeting_start, last_merged_meeting_finish = merged_meetings[-1]

        # If the current meeting's start time collides with last meeting's
        # finish time, then merge the end time of the later
        if current_start <= last_merged_meeting_finish:
            merged_meetings[-1] = ( last_merged_meeting_start,
                                    max(last_merged_meeting_finish, current_finish) )

        else:
            # Add the current meeting to the merged list since they don't overlap
            merged_meetings.append((current_start, current_finish))


    return merged_meetings


# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
