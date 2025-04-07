from django.db import models

class IDProof(models.Model):

    id_choices = {
        "drivers_license": "Drivers License",
        "govt_id": "Province Issue ID",
        "pr_card": "Permanent Residence Card",
        "passport": "Valid Passport",
        "other": "Other"
    }
    
    id_type = models.CharField(blank=True, null=True, choices=id_choices)
    id_number = models.IntegerField(blank=True, null=True)
    id_picture = models.FileField(upload_to="id_uploads/", help_text=".jpg, .jpeg, .png, .pdf files allowed")

    def __str__(self):
        return f"{self.id}"

