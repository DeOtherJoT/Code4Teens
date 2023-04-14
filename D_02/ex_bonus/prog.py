from datetime import datetime
import pytz

local_timezone = pytz.timezone('Asia/Kuala_Lumpur')
local_time = datetime.now(tz=local_timezone)

print(local_time.time())