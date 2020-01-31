from fcm_django.models import FCMDevice

device = FCMDevice.objects.all().first()

device.send_message("Title", "Message")
device.send_message(data={"test": "test"})
device.send_message(title="Title", body="Message", icon=..., data={"test": "test"})