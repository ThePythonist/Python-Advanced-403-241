# import jdatetime
# import locale

# locale.setlocale(locale.LC_ALL, jdatetime.FA_LOCALE)
# now = jdatetime.datetime.now().strftime("%A")
# print(now)

# ================================================================================

from persiantools.jdatetime import JalaliDateTime
import pytz

# now = JalaliDateTime.now().strftime("%A")
# print(now)

weekday = JalaliDateTime(1388, 4, 15, 0, 0, 0, 0, pytz.utc).strftime("%A")
print(weekday)
