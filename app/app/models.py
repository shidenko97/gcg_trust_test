from django.db import models


class Pixels(models.Model):
    """Pixels' table model"""

    id = models.IntegerField(primary_key=True)
    action = models.CharField(max_length=64)
    event_time = models.DateTimeField()
    client_id = models.IntegerField()
    mt_account = models.IntegerField()
    client_name = models.TextField()
    brand_name = models.CharField(max_length=64)
    brand_id = models.IntegerField()
    branch_name = models.CharField(max_length=64)
    amount = models.IntegerField()
    currency = models.CharField(max_length=16)
    affiliateId = models.CharField(max_length=64)
    country = models.CharField(max_length=32)
    source = models.CharField(max_length=64)
    method = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    ip = models.CharField(max_length=16)
    affparams1 = models.CharField(max_length=256)
    affparams2 = models.CharField(max_length=256)
    affparams3 = models.CharField(max_length=256)
    affparams4 = models.CharField(max_length=256)

    def get_client_name(self) -> str:
        """Return client fullname or N/A if not exists"""

        client_name = f"{self.first_name} {self.last_name}"

        return client_name if client_name.strip() else "N/A"

    def get_amount(self) -> int:
        """Return amount or 0 if not exists"""

        return self.amount if self.amount else 0

    @classmethod
    def get_actions(cls):
        """Get all actions of pixels"""

        return cls.objects.values_list("action", flat=True).distinct()

    @classmethod
    def get_countries(cls):
        """Get all countries of pixels"""

        return cls.objects.values_list("country", flat=True).distinct()

    class Meta:
        db_table = "pixels"
