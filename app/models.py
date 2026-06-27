from django.db import models

class Helprequest(models.Model):

    ISSUE_TYPE = [
        ('order', 'Order Problem'),
        ('payment', 'Payment Issue'),
        ('delivery', 'Delivery Issue'),
        ('login', 'Login Issue'),
        ('product', 'Product Issue'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    issue_type = models.CharField(max_length=20, choices=ISSUE_TYPE)
    order_id = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField()

    status = models.CharField(
        max_length=20,
        default='pending'
    )

    def __str__(self):
        return f"{self.name} - {self.issue_type}"
    
    
    
class Report(models.Model):
    REPORT_TYPE = [
        ('product', 'Product Issue'),
        ('order', 'Order Issue'),
        ('payment', 'Payment Issue'),
        ('bug', 'Website Bug'),
        ('delivery', 'Delivery Issue'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE)
    order_id = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField()

    status = models.CharField(max_length=20, default="pending")
    
