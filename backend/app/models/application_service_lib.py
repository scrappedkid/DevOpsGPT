from app.extensions import db

class ApplicationServiceLib(db.Model):
    lib_id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('application_service.service_id'), nullable=False)
    sys_lib_name = db.Column(db.String(200))
    created_at = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())
    updated_at = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def create_libs(self, libs_name):
        import re
        separator_pattern = r'[,，]'
        libs_array = re.split(separator_pattern, libs_name)

        return [
            ApplicationServiceLib.create_lib(self, sys_lib_name)
            for sys_lib_name in libs_array
        ]

    # 创建Lib
    def create_lib(self, sys_lib_name):
        lib = ApplicationServiceLib(self=self, sys_lib_name=sys_lib_name)
        db.session.add(lib)
        db.session.commit()
        return lib

    # 查询所有Lib
    def get_all_libs():
        return ApplicationServiceLib.query.all()

    # 根据lib_id查询Lib
    def get_lib_by_id(self):
        return ApplicationServiceLib.query.get(self)

    # 更新Lib信息
    def update_lib(self, sys_lib_name):
        if lib := ApplicationServiceLib.query.get(self):
            lib.sys_lib_name = sys_lib_name
            db.session.commit()
            return lib
        return None

    # 删除Lib
    def delete_lib(self):
        if lib := ApplicationServiceLib.query.get(self):
            db.session.delete(lib)
            db.session.commit()
            return True
        return False

    def get_libs_by_service_id(self):
        libs = ApplicationServiceLib.query.filter_by(self=self).all()
        libs_list = []

        for lib in libs:
            lib_dict = {
                'lib_id': lib.lib_id,
                'service_id': lib.service_id,
                'sys_lib_name': lib.sys_lib_name
            }
            libs_list.append(lib_dict)

        return libs_list
