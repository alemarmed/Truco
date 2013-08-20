# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Product.categories'
        db.add_column('core_product', 'categories',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['core.Category']),
                      keep_default=False)

        # Adding field 'Product.created_by'
        db.add_column('core_product', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['core.Manager']),
                      keep_default=False)

        # Removing M2M table for field categories on 'Product'
        db.delete_table('core_product_categories')

        # Adding field 'Offer.manager'
        db.add_column('core_offer', 'manager',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['core.Manager']),
                      keep_default=False)

        # Adding field 'Store.owner'
        db.add_column('core_store', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['core.Manager']),
                      keep_default=False)

        # Removing M2M table for field owners on 'Store'
        db.delete_table('core_store_owners')


    def backwards(self, orm):
        # Deleting field 'Product.categories'
        db.delete_column('core_product', 'categories_id')

        # Deleting field 'Product.created_by'
        db.delete_column('core_product', 'created_by_id')

        # Adding M2M table for field categories on 'Product'
        db.create_table('core_product_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm['core.product'], null=False)),
            ('category', models.ForeignKey(orm['core.category'], null=False))
        ))
        db.create_unique('core_product_categories', ['product_id', 'category_id'])

        # Deleting field 'Offer.manager'
        db.delete_column('core_offer', 'manager_id')

        # Deleting field 'Store.owner'
        db.delete_column('core_store', 'owner_id')

        # Adding M2M table for field owners on 'Store'
        db.create_table('core_store_owners', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('store', models.ForeignKey(orm['core.store'], null=False)),
            ('manager', models.ForeignKey(orm['core.manager'], null=False))
        ))
        db.create_unique('core_store_owners', ['store_id', 'manager_id'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.brand': {
            'Meta': {'object_name': 'Brand'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lowcost': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'property_of': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Store']", 'null': 'True'})
        },
        'core.category': {
            'Meta': {'object_name': 'Category'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Category']", 'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'core.category_attr': {
            'Meta': {'object_name': 'Category_attr'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_required': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'core.city': {
            'Meta': {'object_name': 'City'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Province']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'core.consumer': {
            'Meta': {'object_name': 'Consumer'},
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'token_expiration': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'core.country': {
            'Meta': {'object_name': 'Country'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'core.list': {
            'Meta': {'object_name': 'List'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'my_lists'", 'to': "orm['core.Consumer']"}),
            'routed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'core.list_item': {
            'Meta': {'object_name': 'List_item'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.List']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Product']", 'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'vproduct': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Virtual_product']", 'null': 'True'})
        },
        'core.manager': {
            'Meta': {'object_name': 'Manager'},
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nif': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'core.offer': {
            'Meta': {'object_name': 'Offer'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_from': ('django.db.models.fields.DateField', [], {}),
            'date_to': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manager': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Manager']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'offer_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'x': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'y': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'})
        },
        'core.place': {
            'Meta': {'object_name': 'Place'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.City']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Store']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        },
        'core.place_has_product': {
            'Meta': {'object_name': 'Place_has_product'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Place']", 'null': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Product']"}),
            'pvp': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Store']", 'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'core.product': {
            'Meta': {'object_name': 'Product'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Brand']", 'null': 'True'}),
            'categories': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Category']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Manager']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'size_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'size_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'core.product_discount': {
            'Meta': {'object_name': 'Product_discount'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'offer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Offer']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Product']"})
        },
        'core.province': {
            'Meta': {'object_name': 'Province'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Country']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'core.store': {
            'Meta': {'object_name': 'Store'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Manager']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'core.virtual_product': {
            'Meta': {'object_name': 'Virtual_product'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Brand']", 'null': 'True'}),
            'categories': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Category']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'size_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'size_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']