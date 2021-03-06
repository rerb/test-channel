from django.db import models


class Test(models.Model):

    name = models.CharField(max_length=512, db_index=True)


class TestResult(models.Model):

    FAILURE = "failure"
    ERROR = "error"
    SUCCESS = "success"

    test = models.ForeignKey(Test, related_name="results")
    status = models.CharField(max_length=24, db_index=True)

    @classmethod
    def get_num_failures(cls):
        return cls.objects.filter(status=cls.FAILURE).count()

    @classmethod
    def get_num_errors(cls):
        return cls.objects.filter(status=cls.ERROR).count()

    @classmethod
    def get_num_successes(cls):
        return cls.objects.filter(status=cls.SUCCESS).count()

    @classmethod
    def get_num_left(cls):
        return cls.objects.filter(status="").count()

    def fail(self):
        self.status = self.FAILURE
