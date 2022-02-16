#learning how logging systems work - bit of a sidequest
import logging 

log = logging.getLogger("mylogger")
handler = logging.FileHandler("logs\\test.log")

log.addHandler(handler)
log.info("info")
log.error("error")
log.error("insert error")