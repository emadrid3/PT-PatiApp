from django.db import models

# Models for Cutting app


class Cutting(models.Model):
    work_table = models.ForeignKey(
        "WorkTable", on_delete=models.CASCADE, related_name="cuts")

    cut_date = models.DateField()

    reference = models.ForeignKey(
        "Reference",
        on_delete=models.CASCADE,
        related_name="cuts"
    )

    quantity_by_reference = models.PositiveIntegerField(
        verbose_name="Cantidad por referencia"
    )

    color = models.ForeignKey(
        "Color",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="cuts"
    )

    quantity_by_color = models.PositiveIntegerField(
        verbose_name="Cantidad por color"
    )

    material = models.ForeignKey(
        "Material",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="cuts"
    )

    size = models.ForeignKey(
        "Size",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="cuts"
    )

    quantity_by_size = models.PositiveIntegerField(
        verbose_name="Cantidad por talla"
    )

    class Meta:
        verbose_name = "Corte"
        verbose_name_plural = "Cortes"

    # def __str__(self):
    #     return f"Corte {self.id} - {self.reference}"

    def __str__(self):
        return (
            f"Corte #{self.id} | "
            f"Mesa: {self.work_table} | "
            f"Fecha: {self.cut_date} | "
            f"Ref: {self.reference} ({self.quantity_by_reference}) | "
            f"Color: {self.color or 'N/A'} ({self.quantity_by_color}) | "
            f"Material: {self.material or 'N/A'} | "
            f"Talla: {self.size or 'N/A'} ({self.quantity_by_size})"
        )

# Submodels for Cutting app


class Size(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Talla"
        verbose_name_plural = "Tallas"
        ordering = ["id"]

    def __str__(self):
        return self.name


class Reference(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Referencia"
        verbose_name_plural = "Referencias"
        ordering = ["id"]

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiales"
        ordering = ["id"]

    def __str__(self):
        return self.name


class WorkTable(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Mesa de Trabajo"
        verbose_name_plural = "Mesas de Trabajo"
        ordering = ["id"]

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colores"
        ordering = ["id"]

    def __str__(self):
        return self.name
