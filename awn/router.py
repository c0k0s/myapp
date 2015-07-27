"""See https://docs.djangoproject.com/en/dev/topics/db/multi-db/#using-routers 
for details on db routers."""

other = ('city')
Database  = 'DatabaseII'
class DatabaseII(object): 
    def db_for_read(self, model, **hints):
        "Point all operations on waybill models to 'other'"
        if model._meta.app_label in other:
            return Database
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on waybill models to 'other'"
        if model._meta.app_label in other:
            return Database
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in waybill is involved"
        if obj1._meta.app_label in other or obj2._meta.app_label in other:
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the waybill app only appears on the 'other' db"
        if db == Database:
            return model._meta.app_label in other
        elif model._meta.app_label in other:
            return False
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """
        if app_label in other:
            return db == Database
        return None



other2 = ()
class DatabaseIII(object): 
    def db_for_read(self, model, **hints):
        "Point all operations on waybill models to 'other2'"
        if model._meta.app_label in other2:
            return 'DatabaseIII'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on waybill models to 'other2'"
        if model._meta.app_label in other2:
            return 'DatabaseIII'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in waybill is involved"
        if obj1._meta.app_label in other2 or obj2._meta.app_label in other2:
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the waybill app only appears on the 'other2' db"
        if db == 'DatabaseIII':
            return model._meta.app_label in other2
        elif model._meta.app_label in other2:
            return False
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """
        if app_label in other2:
            return db == 'DatabaseIII'
        return None

