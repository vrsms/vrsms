from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Suggestion(models.Model):
    """Model definition for Suggestion."""

    title = models.CharField(_('Title'), max_length=50)
    content = models.TextField(_('Content'))
    is_publishable = models.BooleanField(_('Approval Status'), default=False)
    created_at = models.DateTimeField(_('Created at '), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at '), auto_now=True)

    class Meta:
        """Meta definition for Suggestion."""

        verbose_name = 'Suggestion'
        verbose_name_plural = 'Suggestions'

    def __str__(self):
        """Unicode's representation of Suggestion."""
        return self.title
