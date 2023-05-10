
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_tags_remove_tag_name_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags_name', to='product.tag'),
        ),
    ]
