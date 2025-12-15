from django.db import models
from django.utils import timezone

# Models for Cutting app


class Cutting(models.Model):
    # work_table = models.ForeignKey(
    #     "WorkTable", on_delete=models.CASCADE, related_name="cuts")

    # cut_date = models.DateField()

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

    additional_information = models.TextField(
        blank=True, null=True, verbose_name="Información adicional")

    class Meta:
        verbose_name = "Corte"
        verbose_name_plural = "Cortes"

    # def __str__(self):
    #     return f"Corte {self.id} - {self.reference}"

    def __str__(self):
        return (
            f"Corte #{self.id} | "
            # f"Mesa: {self.work_table} | "
            # f"Fecha: {self.cut_date} | "
            f"Ref: {self.reference} ({self.quantity_by_reference}) | "
            f"Color: {self.color or 'N/A'} ({self.quantity_by_color}) | "
            f"Material: {self.material or 'N/A'} | "
            f"Quantity: {self.quantity_by_size} | "
            f"Talla: {self.size or 'N/A'} ({self.quantity_by_size})"
        )
# ------------------ Submodels ------------------ #
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


class WorkShop(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre del taller")

    # STATUS_CHOICES = [
    #     ('in_process', 'En proceso'),
    #     ('ready', 'Listo'),
    #     ('returned', 'Devuelto'),
    #     ('rejected', 'Rechazado'),
    # ]

    # reference = models.ForeignKey(
    #     Reference,
    #     on_delete=models.CASCADE,
    #     related_name="workshop_assignments",
    #     verbose_name="Tipo de prenda asignada",
    #     default=1
    # )

    # quantity_assigned = models.PositiveIntegerField(
    #     verbose_name="Cantidad asignada", default=0
    # )

    # estimated_delivery_date = models.DateField(
    #     verbose_name="Fecha estimada de entrega",  default=timezone.now)

    # status = models.CharField(
    #     max_length=20,
    #     choices=STATUS_CHOICES,
    #     default='in_process',
    #     verbose_name="Estado"
    # )

    # description = models.TextField(
    #     blank=True, null=True, verbose_name="Descripción")

    class Meta:
        verbose_name = "Asignar Taller"
        verbose_name_plural = "Asignaciones de Talleres"
        ordering = ["id"]

    def __str__(self):
        return self.name
    # def __str__(self):
    #     return f"{self.name} - {self.reference.name} ({self.quantity_assigned})"


class CuttingAssignment(models.Model):

    # New Schemeing for Cutting Assignment Model
    cutting = models.ForeignKey(
        Cutting,
        on_delete=models.CASCADE,
        related_name="assignments",
        verbose_name="Lote"
    )

    workshop = models.ForeignKey(
        WorkShop,
        on_delete=models.CASCADE,
        related_name="assignments",
        verbose_name="Taller asignado"
    )

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    # Cutting batch
    cutting = models.ForeignKey(
        "Cutting",
        on_delete=models.CASCADE,
        related_name="assignments",
        verbose_name="Cutting"
    )

    # Assigned quantities
    quantity_by_color = models.PositiveIntegerField(
        verbose_name="Assigned Quantity by Color"
    )

    quantity_by_size = models.PositiveIntegerField(
        verbose_name="Assigned Quantity by Size"
    )

    # Assignment status
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name="Status"
    )

    # Optional notes
    notes = models.TextField(
        blank=True,
        null=True,
        verbose_name="Notes"
    )

    # Timestamps
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated at"
    )

    class Meta:
        verbose_name = "Cutting Assignment"
        verbose_name_plural = "Cutting Assignments"
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"Assignment #{self.id} | "
            f"Workshop: {self.work_table} | "
            f"Cutting: {self.cutting} | "
            f"Color Qty: {self.quantity_by_color} | "
            f"Size Qty: {self.quantity_by_size} | "
            f"Status: {self.status}"
        )
    # Old Scheme for Cutting Assignment Model

    # cutting = models.ForeignKey(
    #     Cutting,
    #     on_delete=models.CASCADE,
    #     related_name="assignments",
    #     verbose_name="Lote"
    # )

    # workshop = models.ForeignKey(
    #     WorkShop,
    #     on_delete=models.CASCADE,
    #     related_name="assignments",
    #     verbose_name="Taller asignado"
    # )

    # quantity_assigned = models.PositiveIntegerField(
    #     verbose_name="Cantidad asignada")

    # estimated_delivery_date = models.DateField(
    #     verbose_name="Fecha estimada de entrega")

    # status = models.CharField(
    #     max_length=20,
    #     choices=[
    #         ('in_process', 'En proceso'),
    #         ('ready', 'Listo'),
    #         ('returned', 'Devuelto'),
    #         ('rejected', 'Rechazado')
    #     ],
    #     default='in_process',
    #     verbose_name="Estado"
    # )

    # description = models.TextField(
    #     blank=True, null=True, verbose_name="Descripción")

    # class Meta:
    #     verbose_name = "Asignación de Corte"
    #     verbose_name_plural = "Asignaciones de Cortes"
    #     ordering = ["id"]

    # def __str__(self):
    #     return f"Lote {self.cutting.id} → Taller {self.workshop.name} ({self.quantity_assigned})"
