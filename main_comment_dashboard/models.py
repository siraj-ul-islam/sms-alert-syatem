from django.db import models

# Create your models here.


class unit_details(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=True, null=True, blank=False, )
    unit_name = models.CharField(max_length=30, null=False, blank=True, )
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.unit_name

    class Meta:
        db_table = 'unit_details'
        # managed = False

class unit_address_details(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=True, null=True, blank=False, )
    unit_details_id = models.ForeignKey(unit_details, on_delete=models.CASCADE)
    unit_address =  models.CharField(max_length=225,  null=True, blank=True, )
    rank_message_sender = models.CharField(max_length=60, null=False, blank=True, )
    phone_number = models.CharField(max_length=30, null=False, blank=True, )
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.unit_address

    class Meta:
        db_table = 'unit_address_details'


class unit_comment_details(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=True, null=True, blank=False, )
    unit_address_details_id = models.ForeignKey(unit_details, on_delete=models.CASCADE)
    problem = models.CharField(max_length=225,  null=True, blank=True, )
    remarks = models.CharField(max_length=225, null=True, blank=True, )
    car_type = models.CharField(max_length=225, null=True, blank=True, )
    vehicle_no = models.CharField(max_length=225,  null=False, blank=True, )
    driver_name = models.CharField(max_length=225,  null=False, blank=True, )
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = 'unit_comment_details'
        # managed = False