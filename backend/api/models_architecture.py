from django.db import models


class ArchDynasty(models.Model):
    """朝代模型"""
    did = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=45, verbose_name="朝代名称")
    period = models.CharField(max_length=100, verbose_name="时期", blank=True)
    description = models.TextField(verbose_name="朝代简介", blank=True)
    
    class Meta:
        db_table = 'architecture_dynasty'
        verbose_name = "朝代"
        verbose_name_plural = "朝代"
    
    def __str__(self):
        return self.dname


class ArchRegion(models.Model):
    """地域模型（替代省份）"""
    rid = models.IntegerField(primary_key=True)
    rname = models.CharField(max_length=45, verbose_name="地域名称")
    description = models.TextField(verbose_name="地域特色", blank=True)
    
    class Meta:
        db_table = 'architecture_region'
        verbose_name = "地域"
        verbose_name_plural = "地域"
    
    def __str__(self):
        return self.rname


class ArchStructureType(models.Model):
    """建筑结构类型"""
    tid = models.IntegerField(primary_key=True)
    tname = models.CharField(max_length=45, verbose_name="类型名称")
    description = models.TextField(verbose_name="类型描述", blank=True)
    
    class Meta:
        db_table = 'architecture_structure_type'
        verbose_name = "结构类型"
        verbose_name_plural = "结构类型"
    
    def __str__(self):
        return self.tname


class AncientBuilding(models.Model):
    """古建筑模型"""
    bid = models.IntegerField(primary_key=True)
    bname = models.CharField(max_length=100, verbose_name="建筑名称")
    dynasty = models.ForeignKey(ArchDynasty, on_delete=models.CASCADE, verbose_name="所属朝代")
    region = models.ForeignKey(ArchRegion, on_delete=models.CASCADE, verbose_name="所属地域")
    structure_type = models.ForeignKey(ArchStructureType, on_delete=models.CASCADE, verbose_name="结构类型")
    
    # 建筑特征
    roof_type = models.CharField(max_length=50, verbose_name="屋顶形式", blank=True)  # 庑殿顶、歇山顶等
    dougong_style = models.CharField(max_length=50, verbose_name="斗拱样式", blank=True)
    
    # 位置信息
    longitude = models.FloatField(verbose_name="经度")
    latitude = models.FloatField(verbose_name="纬度")
    address = models.CharField(max_length=200, verbose_name="详细地址", blank=True)
    
    # 描述信息
    introduction = models.TextField(verbose_name="建筑简介")
    historical_value = models.TextField(verbose_name="历史价值", blank=True)
    architectural_features = models.TextField(verbose_name="建筑特色", blank=True)
    
    # 梁思成相关
    liang_sicheng_note = models.TextField(verbose_name="梁思成评价", blank=True)
    
    # 媒体资源
    image_url = models.CharField(max_length=500, verbose_name="图片URL", blank=True)
    model_3d_url = models.CharField(max_length=500, verbose_name="3D模型URL", blank=True)
    
    class Meta:
        db_table = 'architecture_building'
        verbose_name = "古建筑"
        verbose_name_plural = "古建筑"
    
    def __str__(self):
        return self.bname


class ArchitecturalElement(models.Model):
    """建筑元素（斗拱、屋顶等）知识库"""
    eid = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=100, verbose_name="元素名称")
    category = models.CharField(max_length=50, verbose_name="类别")  # 斗拱、屋顶、柱式等
    
    # 梁思成《中国建筑史》原文引用
    original_text = models.TextField(verbose_name="原文引用", blank=True)
    explanation = models.TextField(verbose_name="详细解释")
    
    # 结构说明
    structure_description = models.TextField(verbose_name="结构说明", blank=True)
    function_description = models.TextField(verbose_name="功能说明", blank=True)
    
    # 演变历史
    evolution = models.TextField(verbose_name="演变历史", blank=True)
    
    # 媒体资源
    image_url = models.CharField(max_length=500, verbose_name="示意图URL", blank=True)
    diagram_url = models.CharField(max_length=500, verbose_name="结构图URL", blank=True)
    
    class Meta:
        db_table = 'architecture_element'
        verbose_name = "建筑元素"
        verbose_name_plural = "建筑元素"
    
    def __str__(self):
        return self.ename


class ArchUserPreference(models.Model):
    """用户偏好（用于个性化推荐）"""
    user = models.ForeignKey('ArchUsers', on_delete=models.CASCADE)
    dynasty_preference = models.JSONField(default=dict, verbose_name="朝代偏好")
    region_preference = models.JSONField(default=dict, verbose_name="地域偏好")
    type_preference = models.JSONField(default=dict, verbose_name="类型偏好")
    
    class Meta:
        db_table = 'architecture_user_preference'


class ArchUsers(models.Model):
    """用户模型"""
    username = models.CharField(max_length=100, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=128, verbose_name="密码")
    email = models.EmailField(max_length=254, verbose_name="邮箱")
    like = models.CharField(max_length=500, verbose_name="兴趣标签", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'architecture_users'
        verbose_name = "用户"
        verbose_name_plural = "用户"


class ArchitecturalLiterature(models.Model):
    """古建筑文献资料"""
    lid = models.IntegerField(primary_key=True)
    lname = models.CharField(max_length=200, verbose_name="文献名称")
    author = models.CharField(max_length=100, verbose_name="作者")
    dynasty = models.CharField(max_length=50, verbose_name="朝代/时期", blank=True)
    publish_year = models.IntegerField(verbose_name="出版年份", null=True, blank=True)
    
    # 文献类型
    literature_type = models.CharField(max_length=50, verbose_name="文献类型", 
                                       choices=[
                                           ('ancient', '古代典籍'),
                                           ('modern', '现代著作'),
                                           ('survey', '调查报告'),
                                           ('textbook', '教材'),
                                           ('collection', '文集')
                                       ])
    
    # 内容信息
    summary = models.TextField(verbose_name="内容摘要")
    key_points = models.TextField(verbose_name="核心观点", blank=True)
    contributions = models.TextField(verbose_name="学术贡献", blank=True)
    
    # 版本信息
    publisher = models.CharField(max_length=100, verbose_name="出版社", blank=True)
    edition = models.CharField(max_length=50, verbose_name="版本", blank=True)
    pages = models.IntegerField(verbose_name="页数", null=True, blank=True)
    
    # 相关建筑
    related_buildings = models.ManyToManyField(
        AncientBuilding, 
        blank=True, 
        verbose_name="相关建筑",
        db_table='architecture_literature_building'
    )
    
    # 媒体资源
    cover_image = models.CharField(max_length=500, verbose_name="封面图片", blank=True)
    pdf_url = models.CharField(max_length=500, verbose_name="PDF链接", blank=True)
    
    class Meta:
        db_table = 'architecture_literature'
        verbose_name = "古建筑文献"
        verbose_name_plural = "古建筑文献"
    
    def __str__(self):
        return f"{self.lname} - {self.author}"
