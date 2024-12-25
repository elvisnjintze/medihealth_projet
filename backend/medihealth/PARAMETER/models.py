from django.db import models
# Create your models here.


class CMPPAR(models.Model):
    CODPAR = models.CharField(max_length=10)  # Correspond à VARCHAR2(10 BYTE)
    CLE = models.CharField(max_length=3)  # Correspond à VARCHAR2(3 BYTE)
    LIBPAR = models.CharField(max_length=30)  # Correspond à VARCHAR2(30 BYTE)
    MEMO = models.CharField(max_length=255, blank=True, null=True)  # Correspond à VARCHAR2(255 BYTE)
    VALC = models.CharField(max_length=30, blank=True, null=True)  # Correspond à VARCHAR2(30 BYTE)
    VALN = models.DecimalField(max_digits=16, decimal_places=4, blank=True, null=True)  # Correspond à NUMBER(16,4)
    VALT = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # Correspond à NUMBER(5,2)
    DATE_CREAT = models.DateField()  # Correspond à DATE
    UTIL_CREAT = models.CharField(max_length=5)  # Correspond à VARCHAR2(5 BYTE)
    DATE_MODIF = models.DateField(blank=True, null=True)  # Correspond à DATE
    UTIL_MODIF = models.CharField(max_length=5, blank=True, null=True)  # Correspond à VARCHAR2(5 BYTE)

    class Meta:
        db_table = 'CMPPAR'  # Nom de la table dans la base de données
        managed = True  # Django peut gérer cette table
        unique_together = (('CODPAR', 'CLE'),)  # Correspond à la contrainte PRIMARY KEY ("CODPAR", "CLE")
        verbose_name = "CMPPAR"
        verbose_name_plural = "CMPPARs"

    def __str__(self):
        return f"{self.CODPAR} - {self.CLE} - {self.LIBPAR}"
