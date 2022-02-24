from pydantic import BaseModel as PydanticBaseModel
from pydantic import Field
from typing import Literal
import joblib
import pandas as pd
from fastapi import HTTPException




# Una variable binaria puede ser:
# binaria: int = Field(ge=0, le=1)
# O, binaria: bool
class ModelInput(PydanticBaseModel):
    '''
    Clase que define las entradas del modelo
    
    '''
    Bcpp: int = Field(description='Credito vehícular', ge=0, le=100000000)
    Potencia: int = Field(description='Potencia',ge=0, le=1000)
    Cilindraje: int = Field(description='Cilindraje',ge=0, le=999999)
    PesoCategoria: int = Field(description='PesoCategoria',ge=0, le=2)
    Marca: Literal['ALEKO', 'AMERICAN MOTOR', 'AUTECO', 'AROCARPATI', 'ASIA', 'AUDI', 'AUTOCAR', 
         'BMW', 'DINA', 'BUICK', 'CAGIVA', 'CADILLAC', 'CORCEL', 'CHEVROLET', 'CHRYSLER', 'CITROEN',
         'DACIA', 'DAEWOO', 'DAIHATSU', 'DERBI', 'DODGE', 'DUCATI', 'FIAT', 'FREIGHTLINER', 'FORD',
         'MOTO GUZZI', 'HYUNDAI', 'HARLEY DAVIDSON', 'HONDA', 'IFA', 'INTERNATIONAL', 'HINO', 'ISUZU',
         'JAWA', 'JAGUAR', 'JEEP', 'KAMAZ', 'KENWORTH', 'KAWASAKI', 'KIA', 'KRAZ', 'LADA', 'MARMON',
         'LANCIA', 'HYOSUNG', 'LAND ROVER', 'MORINI', 'MACK', 'MAZDA', 'MERCEDES BENZ', 'MINI', 'MERCURY',
         'MG', 'MITSUBISHI', 'NISSAN', 'PEGASO', 'OLTCIT', 'PEUGEOT', 'PAZ', 'PIAGGIO', 'BEIJING',
         'PONTIAC', 'PORSCHE', 'RENAULT', 'SCANIA', 'SEAT', 'SSANGYONG', 'SISU', 'SKODA', 'SUBARU', 
         'SUZUKI', 'TAVRIA', 'TOYOTA', 'UAZ', 'VOLKSWAGEN', 'VOLGA', 'VOLVO', 'WESTERN STAR', 'YUGO', 
         'YAMAHA', 'TATA', 'KYMCO', 'IVECO', 'AGRALE', 'CHANA', 'CHERY', 'HAFEI', 'RENNO', 'SAICWULING',
         'CHANGHE', 'BYD', 'HALEI', 'JAC', 'TITANIA', 'ZHONGXING', 'AMPLE', 'GLOW', 'VERUCCI', 'JIALING',
         'GERLAP', 'DAYANG', 'JINCHENG', 'GEELY', 'INFINITI', 'JINGLONG', 'UTILITY', 'KEEWAY', 'KYOTO', 
         'FIRENZE', 'SERVICHASIS', 'HONLEI', 'OPEL', 'TRAILER SANDER', 'TECNIPESADOS', 'KAZUKI', 
         'UNITED MOTORS', 'PIONEER', 'TALLER OVEL', 'TRACTEC', 'AYCO', 'XINKAI', 'DFSK/DFM/DFZL', 'YINGANG',
         'SIGMA', 'TECNICAR', 'APRILIA',   'RAFAEL ESCOBAR', 'SHINERAY', 'TODO TRAIL', 'QINGQI', 'GOLDEN DRAGON',
         'USW MOTORS', 'STELL TRAILERS', 'XIANFENG', 'TRAYCOL', 'JMC', 'AKT', 'MANETRA', 'JINFENG', 'BRP CAN AM',
         'GREAT WALL MOTOR', 'INDUCAM JC', 'HEIL', 'WABASH NATIONAL', 'FALCON', 'PETERBILT', 'MAXMOTOR', 'KTM', 
         'GOMOTOR', 'CANACOL', 'GERMAR GMG', 'BORGO', 'TALLERES MILTON', 'SUKIDA', 'ZAHAV', 'ESTEMCO', 'NITRO',
         'ITANREM', 'SERVI VOLCOS', 'CMC', 'TRAILERS DE SANTANDER', 'DUST', 'FOTON', 'CEDAL', 'VENTO', 'XINGYUE',
         'ROMARCO', 'FAMERS', 'INTRAILER', 'FEGAM', 'TRAILERS TULUA', 'MECANICOS UNIDOS', 'IMECOL', 'RHINO',
         'GREAT DANE', 'TONGKO', 'TRAYVOCOL', 'HIDROAMERICA', 'METAL INOX', 'YAKIMA', 'WANXIN', 'SERVITRACK', 
         'IMEVA', 'GAZ', 'MORENO', 'INDUSTRIAS BERMEO', 'CONSTRUTRAILER', 'INCALLES COLOMBIA','GUERCAR', 'EAGLE TRUCK',
         'TRAILERS DE ANTIOQUIA', 'BISON TRUCK', 'KAYAK', 'INCA FRUEHAUF', 'PRISMA', 'PANAMERICANA', 'ZOTYE',
         'EL TRAILERO', 'ORLTRAILER', 'INOX MEC', 'METALCONT', 'HUMMER', 'AUPACO', 'INCOLTRAILERS', 'IMCOLTRANS',
         'LIFAN', 'TECNOTRAILERS', 'INDUROC', 'APONCAR', 'TALLERES CESPEDES', 'HIGER', 'CARROCERIAS MODERNA', 
         'MD BIKES', 'TALLER T F S', 'SAAB', 'SANYA', 'EL SOL', 'TIANMA', 'MTK', 'AMC', 'WCR', 'ZQ MOTORS', 
         'ALCAR', 'ACB', 'SUKYAMA', 'FAW AMI', 'CHANGFENG', 'SKYGO', 'FERRELAMINAS', 'INDUGWEST', 'ANDITRAILERS',
         'INDUREMOLQUES', 'TRAILERS SUPERIOR', 'EQUITRAILER', 'BAYONA TRAILER', 'FULL TRAILER', 'GUZI', 'STEYR',
         'SHUANGHUAN', 'HONGXING', 'MUDAN', 'CARROCERIAS JAGUER', 'TECNITANQUES', 'TODOTRAILERS', 'ZONGSHEN',
         'DITE', 'RANDON', 'INDUVOLCOS', 'TX MOTORS', 'OXITANQUES', 'TALLERES CEPEDA','MULTITRAILERS', 
         'EUROSTAR D`LONG', 'EAGLE CARGO', 'SER REMOLQUES', 'INSAR', 'TRAILERS DE LA SABANA', 'TRAILERS HERCULES',
         'SERVITRAILER', 'REPATRAILERSVAN', 'SAN MARCOS', 'CAPRI', 'TVS', 'COLTRAILER', 'EL CHINO BERNA', 'LOHR',
         'TECNITRACS', 'POLARIS', 'CILINDRAULICOS', 'METALLICA', 'UFO', 'MACTRAILERS', 'DORSEY', 'GONOW', 'ONEIDA',
         'RODRIREMOLQUES', 'ATM', 'VOLCOS UFF', 'FMI', 'APOLO', 'CONSTRUTANQUES', 'BAW', 'VYR CARVAJAL', 'CONALCAR',
         'GREMCAR', 'TRAILERS & TRAILERS', 'INDUCAPI', 'TECNISANDER', 'JINBEI', 'CONTAPA', 'GESMET', 'EL ABARCO',
         'SOYAT', 'TECNITRAILER', 'ZHONGNENG', 'SATURN', 'TEMPEST', 'TECNITRAILERS', 'TALLERES PACHON', 'LA QUINTA RUEDA',
         'GAS GAS', 'PASSAGGIO', 'UKM', 'SACHS', 'YUTONG', 'SG INGENIERIA', 'NON PLUS ULTRA', 'VESPA', 'EUROPAMOTOS',
         'SYM', 'CYAN', 'ACURA', 'LEXUS', 'AG', 'SINOTRUK', 'FONTAINE', 'FRANCOCOL', 'BRONTO', 'SMC', 'HUSQVARNA',
         'TMD', 'LANDWIND', 'PROCEIN', 'ROVER', 'MASERATI', 'ALFA ROMEO', 'YAKEY', 'FERRARI', 'ROYAL ENFIELD', 
         'AMERICAN TRAYLER', 'GMC', 'YAXING', 'SCION', 'AVA', 'TRIUMPH', 'T-KING', 'HAIMA', 'ZNA', 'HUANGHAI', 
         'MAHINDRA', 'HAOJIANG', 'LINCOLN', 'HUALIN', 'ARCTIC CAT', 'DADI', 'BENELLI', 'CARMEX', 'MOTO ABC',
         'BRILLIANCE', 'LML', 'JOYLONG', 'CIMC', 'MAXUS', 'INCOLTANQUES', 'DFAC', 'SMART', 'MV AGUSTA', 'BAIC',
         'LMX', 'CHANGAN', 'DONGBEN', 'YUEJIN-NAVECO', 'HERO', 'VICTORY', 'VAISAND', 'FUSO', 'DAF',
         'STÄRKER', 'SCOMADI', 'HAOJUE', 'DS']
    Clase: Literal['BUS / BUSETA / MICROBUS', 'CAMION', 'CARROTANQUE', 'CHASIS',
       'FURGON', 'REMOLCADOR', 'VOLQUETA', 'CAMPERO', 'AUTOMOVIL',
       'REMOLQUE', 'MOTOCICLETA', 'PICKUP SENCILLA', 'CAMIONETA PASAJ.',
       'FURGONETA', 'MOTOCARRO', 'PICKUP DOBLE CAB', 'CAMIONETA REPAR',
       'ISOCARRO', 'UNIMOG']
    Fechas: Literal['1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977',
       '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
        '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', 
        '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', 
        '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017',
       '2018']
    

    # OPCIONAL: Poner el ejemplo para que en la documentación ya puedan de una lanzar la predicción.
    class Config:
        schema_extra = {
            "example": {
                'Bcpp': 45682,
                'Potencia': 500,
                'Cilindraje': 125,
                'PesoCategoria': 1,
                'Marca': "BMW",
                'Clase': "CAMION",
                'Fechas': "2005"
            }
        }


class ModelOutput(PydanticBaseModel):
    '''
    Clase que define las salidas del modelo
    '''
    precio: int = Field(description='Precio de referencia')

    class Config:
        schema_extra = {
            "example": {
                'precio': 11612.4
            }
        }


class APIModelBackEnd():
    '''
    Esta clase maneja el back end de nuestro modelo de Machine Learning para la API en FastAPI
    '''

    def __init__(self,Bcpp,Potencia,Cilindraje,PesoCategoria,Marca,Clase,Fechas):
        '''
        Este método se usa al instanciar las clases

        Aquí, hacemos que pida los mismos parámetros que tenemos en ModelInput.

        '''
        
        self.Bcpp = Bcpp
        self.Potencia = Potencia
        self.Cilindraje = Cilindraje
        self.PesoCategoria = PesoCategoria
        self.Marca = Marca
        self.Clase = Clase
        self.Fechas = Fechas

    def _load_model(self, model_filename: str = 'modelRF1.pkl'):
        '''
        Clase para cargar el modelo. Es una forma exótica de correr joblib.load pero teniendo funcionalidad con la API.
        Este método seguramente no lo van a cambiar, y si lo cambian, cambian el valor por defecto del string
        '''
        # Asignamos a un atributo el nombre del archivo
        self.model_filename = model_filename
        try:
            # Se intenta cargar el modelo
            self.model = joblib.load(self.model_filename)
        except Exception:
            # Si hay un error, se levanda una Exception de HTTP diciendo que no se encontró el modelo
            raise HTTPException(status_code=404, detail=f'Modelo con el nombre {self.model_filename} no fue encontrado')
        # Si todo corre ok, imprimimos que cargamos el modelo
        print(f"El modelo '{self.model_filename}' fue cargado exitosamente")

    def _prepare_data(self):
        '''
        Clase de preparar lo datos.
        Este método convierte las entradas en los datos que tenían en X_train y X_test.

        Miren el orden de las columnas de los datos antes de su modelo.
        Tienen que recrear ese orden, en un dataframe de una fila.

        '''
        # Pueden manejar así las variables categoricas.
        # Revisen los X!!! De eso depende que valores hay aquí.
        # Para ver más o menos que valores pueden ser, en un data frame se le aplico pd.get_dummies, corran algo como:
        # X_test[[col for col in X_test.columns if "nombre de columna" in col]].drop_duplicates()
        
        f2 = ['Bcpp', 'Potencia', 'Cilindraje', 'PesoCategoria', 'Marca_ACURA', 
                                    'Marca_AG', 'Marca_AGRALE', 'Marca_AKT', 'Marca_ALCAR', 'Marca_ALEKO', 'Marca_ALFA ROMEO', 
                                    'Marca_AMC', 'Marca_AMERICAN MOTOR', 'Marca_AMERICAN TRAYLER', 'Marca_AMPLE', 'Marca_ANDITRAILERS',
                                     'Marca_APOLO', 'Marca_APONCAR', 'Marca_APRILIA', 'Marca_ARCTIC CAT', 'Marca_AROCARPATI', 'Marca_ASIA',
                                     'Marca_ATM', 'Marca_AUDI', 'Marca_AUPACO', 'Marca_AUTECO', 'Marca_AUTOCAR', 'Marca_AVA',
                                     'Marca_AYCO', 'Marca_BAIC', 'Marca_BAW', 'Marca_BAYONA TRAILER', 'Marca_BEIJING', 'Marca_BENELLI',
                                     'Marca_BISON TRUCK', 'Marca_BMW', 'Marca_BORGO', 'Marca_BRILLIANCE', 'Marca_BRONTO', 'Marca_BRP CAN AM',
                                     'Marca_BUICK', 'Marca_BYD', 'Marca_CADILLAC', 'Marca_CAGIVA', 'Marca_CANACOL', 'Marca_CAPRI', 'Marca_CARMEX',
                                     'Marca_CARROCERIAS JAGUER', 'Marca_CARROCERIAS MODERNA', 'Marca_CEDAL', 'Marca_CHANA', 'Marca_CHANGAN', 'Marca_CHANGFENG',
                                     'Marca_CHANGHE', 'Marca_CHERY', 'Marca_CHEVROLET', 'Marca_CHRYSLER', 'Marca_CILINDRAULICOS', 'Marca_CIMC', 'Marca_CITROEN',
                                     'Marca_CMC', 'Marca_COLTRAILER', 'Marca_CONALCAR', 'Marca_CONSTRUTANQUES', 'Marca_CONSTRUTRAILER', 'Marca_CONTAPA',
                                     'Marca_CORCEL', 'Marca_CYAN', 'Marca_DACIA', 'Marca_DADI', 'Marca_DAEWOO', 'Marca_DAF', 'Marca_DAIHATSU', 'Marca_DAYANG',
                                     'Marca_DERBI', 'Marca_DFAC', 'Marca_DFSK/DFM/DFZL', 'Marca_DINA', 'Marca_DITE', 'Marca_DODGE', 'Marca_DONGBEN', 'Marca_DORSEY',
                                     'Marca_DS', 'Marca_DUCATI', 'Marca_DUST', 'Marca_EAGLE CARGO', 'Marca_EAGLE TRUCK', 'Marca_EL ABARCO', 'Marca_EL CHINO BERNA',
                                     'Marca_EL SOL', 'Marca_EL TRAILERO', 'Marca_EQUITRAILER', 'Marca_ESTEMCO', 'Marca_EUROPAMOTOS', 'Marca_EUROSTAR D`LONG',
                                    'Marca_FALCON', 'Marca_FAMERS', 'Marca_FAW AMI', 'Marca_FEGAM', 'Marca_FERRARI', 'Marca_FERRELAMINAS', 'Marca_FIAT',
                                     'Marca_FIRENZE', 'Marca_FMI', 'Marca_FONTAINE', 'Marca_FORD', 'Marca_FOTON', 'Marca_FRANCOCOL', 'Marca_FREIGHTLINER',
                                    'Marca_FULL TRAILER', 'Marca_FUSO', 'Marca_GAS GAS', 'Marca_GAZ', 'Marca_GEELY', 'Marca_GERLAP', 'Marca_GERMAR GMG', 'Marca_GESMET',
                                     'Marca_GLOW', 'Marca_GMC', 'Marca_GOLDEN DRAGON', 'Marca_GOMOTOR', 'Marca_GONOW', 'Marca_GREAT DANE', 'Marca_GREAT WALL MOTOR', 'Marca_GREMCAR',
                                     'Marca_GUERCAR', 'Marca_GUZI', 'Marca_HAFEI', 'Marca_HAIMA', 'Marca_HALEI', 'Marca_HAOJIANG', 'Marca_HAOJUE', 'Marca_HARLEY DAVIDSON',
                                     'Marca_HEIL', 'Marca_HERO', 'Marca_HIDROAMERICA', 'Marca_HIGER', 'Marca_HINO', 'Marca_HONDA', 'Marca_HONGXING', 'Marca_HONLEI',
                                     'Marca_HUALIN', 'Marca_HUANGHAI', 'Marca_HUMMER', 'Marca_HUSQVARNA', 'Marca_HYOSUNG', 'Marca_HYUNDAI', 'Marca_IFA',
                                     'Marca_IMCOLTRANS', 'Marca_IMECOL', 'Marca_IMEVA', 'Marca_INCA FRUEHAUF', 'Marca_INCALLES COLOMBIA', 'Marca_INCOLTANQUES',
                                     'Marca_INCOLTRAILERS', 'Marca_INDUCAM JC', 'Marca_INDUCAPI', 'Marca_INDUGWEST', 'Marca_INDUREMOLQUES', 'Marca_INDUROC', 'Marca_INDUSTRIAS BERMEO',
                                     'Marca_INDUVOLCOS', 'Marca_INFINITI', 'Marca_INOX MEC', 'Marca_INSAR', 'Marca_INTERNATIONAL', 'Marca_INTRAILER', 'Marca_ISUZU',
                                     'Marca_ITANREM', 'Marca_IVECO', 'Marca_JAC', 'Marca_JAGUAR', 'Marca_JAWA', 'Marca_JEEP', 'Marca_JIALING', 'Marca_JINBEI', 'Marca_JINCHENG',
                                     'Marca_JINFENG', 'Marca_JINGLONG', 'Marca_JMC', 'Marca_JOYLONG', 'Marca_KAMAZ', 'Marca_KAWASAKI', 'Marca_KAYAK', 'Marca_KAZUKI',
                                     'Marca_KEEWAY', 'Marca_KENWORTH', 'Marca_KIA', 'Marca_KRAZ', 'Marca_KTM', 'Marca_KYMCO', 'Marca_KYOTO', 'Marca_LA QUINTA RUEDA', 'Marca_LADA',
                                     'Marca_LANCIA', 'Marca_LAND ROVER', 'Marca_LANDWIND', 'Marca_LEXUS', 'Marca_LIFAN', 'Marca_LINCOLN', 'Marca_LML',
                                    'Marca_LMX', 'Marca_LOHR', 'Marca_MACK', 'Marca_MACTRAILERS', 'Marca_MAHINDRA', 'Marca_MANETRA', 'Marca_MARMON',
                                    'Marca_MASERATI', 'Marca_MAXMOTOR', 'Marca_MAXUS', 'Marca_MAZDA', 'Marca_MD BIKES', 'Marca_MECANICOS UNIDOS', 'Marca_MERCEDES BENZ',
                                     'Marca_MERCURY', 'Marca_METAL INOX', 'Marca_METALCONT', 'Marca_METALLICA', 'Marca_MG', 'Marca_MINI', 'Marca_MITSUBISHI',
                                     'Marca_MORENO', 'Marca_MORINI', 'Marca_MOTO ABC', 'Marca_MOTO GUZZI', 'Marca_MTK', 'Marca_MUDAN', 'Marca_MULTITRAILERS',
                                     'Marca_MV AGUSTA', 'Marca_NISSAN', 'Marca_NITRO', 'Marca_NON PLUS ULTRA', 'Marca_OLTCIT', 'Marca_ONEIDA', 'Marca_OPEL',
                                     'Marca_ORLTRAILER', 'Marca_OXITANQUES', 'Marca_PANAMERICANA', 'Marca_PASSAGGIO', 'Marca_PAZ', 'Marca_PEGASO', 'Marca_PETERBILT',
                                     'Marca_PEUGEOT', 'Marca_PIAGGIO', 'Marca_PIONEER', 'Marca_POLARIS', 'Marca_PONTIAC', 'Marca_PORSCHE', 'Marca_PRISMA',
                                     'Marca_PROCEIN', 'Marca_QINGQI', 'Marca_RAFAEL ESCOBAR', 'Marca_RANDON', 'Marca_RENAULT', 'Marca_RENNO', 'Marca_REPATRAILERSVAN',
                                    'Marca_RHINO', 'Marca_RODRIREMOLQUES', 'Marca_ROMARCO', 'Marca_ROVER', 'Marca_ROYAL ENFIELD', 'Marca_SAAB', 'Marca_SACHS',
                                     'Marca_SAICWULING', 'Marca_SAN MARCOS', 'Marca_SANYA', 'Marca_SATURN', 'Marca_SCANIA', 'Marca_SCION', 'Marca_SCOMADI',
                                    'Marca_SEAT', 'Marca_SER REMOLQUES', 'Marca_SERVI VOLCOS', 'Marca_SERVICHASIS', 'Marca_SERVITRACK', 'Marca_SERVITRAILER',
                                    'Marca_SG INGENIERIA', 'Marca_SHINERAY', 'Marca_SHUANGHUAN', 'Marca_SIGMA', 'Marca_SINOTRUK', 'Marca_SISU', 'Marca_SKODA', 'Marca_SKYGO',
                                     'Marca_SMART', 'Marca_SMC', 'Marca_SOYAT', 'Marca_SSANGYONG', 'Marca_STELL TRAILERS', 'Marca_STEYR', 'Marca_STÄRKER', 'Marca_SUBARU',
                                     'Marca_SUKIDA', 'Marca_SUKYAMA', 'Marca_SUZUKI', 'Marca_SYM', 'Marca_T-KING', 'Marca_TALLER OVEL', 'Marca_TALLER T F S',
                                    'Marca_TALLERES CEPEDA', 'Marca_TALLERES CESPEDES', 'Marca_TALLERES MILTON', 'Marca_TALLERES PACHON', 'Marca_TATA',
                                     'Marca_TAVRIA', 'Marca_TECNICAR', 'Marca_TECNIPESADOS', 'Marca_TECNISANDER', 'Marca_TECNITANQUES', 'Marca_TECNITRACS', 'Marca_TECNITRAILER',
                                     'Marca_TECNITRAILERS', 'Marca_TECNOTRAILERS', 'Marca_TEMPEST', 'Marca_TIANMA', 'Marca_TITANIA', 'Marca_TMD', 'Marca_TODO TRAIL', 'Marca_TODOTRAILERS',
                                     'Marca_TONGKO', 'Marca_TOYOTA', 'Marca_TRACTEC', 'Marca_TRAILER SANDER', 'Marca_TRAILERS & TRAILERS', 'Marca_TRAILERS DE ANTIOQUIA', 'Marca_TRAILERS DE LA SABANA',
                                     'Marca_TRAILERS DE SANTANDER', 'Marca_TRAILERS HERCULES', 'Marca_TRAILERS SUPERIOR', 'Marca_TRAILERS TULUA', 'Marca_TRAYCOL', 'Marca_TRAYVOCOL',
                                     'Marca_TRIUMPH', 'Marca_TVS', 'Marca_TX MOTORS', 'Marca_UAZ', 'Marca_UFO', 'Marca_UKM', 'Marca_UNITED MOTORS', 'Marca_USW MOTORS',
                                     'Marca_UTILITY', 'Marca_VAISAND', 'Marca_VENTO', 'Marca_VERUCCI', 'Marca_VESPA', 'Marca_VICTORY', 'Marca_VOLCOS UFF',
                                    'Marca_VOLGA', 'Marca_VOLKSWAGEN', 'Marca_VOLVO', 'Marca_VYR CARVAJAL', 'Marca_WABASH NATIONAL', 'Marca_WANXIN', 'Marca_WCR', 'Marca_WESTERN STAR',
                                     'Marca_XIANFENG', 'Marca_XINGYUE', 'Marca_XINKAI', 'Marca_YAKEY', 'Marca_YAKIMA', 'Marca_YAMAHA', 'Marca_YAXING',
                                     'Marca_YINGANG', 'Marca_YUEJIN-NAVECO', 'Marca_YUGO', 'Marca_YUTONG', 'Marca_ZAHAV', 'Marca_ZHONGNENG', 'Marca_ZHONGXING', 'Marca_ZNA',
                                     'Marca_ZONGSHEN', 'Marca_ZOTYE', 'Marca_ZQ MOTORS', 'Clase_BUS / BUSETA / MICROBUS', 'Clase_CAMION', 'Clase_CAMIONETA PASAJ.', 'Clase_CAMIONETA REPAR', 'Clase_CAMPERO',
                                     'Clase_CARROTANQUE', 'Clase_CHASIS', 'Clase_FURGON', 'Clase_FURGONETA', 'Clase_ISOCARRO', 'Clase_MOTOCARRO', 'Clase_MOTOCICLETA', 'Clase_PICKUP DOBLE CAB',
                                     'Clase_PICKUP SENCILLA', 'Clase_REMOLCADOR', 'Clase_REMOLQUE', 'Clase_UNIMOG', 'Clase_VOLQUETA', 'Fechas_1971', 'Fechas_1972',
                                     'Fechas_1973', 'Fechas_1974', 'Fechas_1975', 'Fechas_1976', 'Fechas_1977', 'Fechas_1978', 'Fechas_1979', 'Fechas_1980',
                                     'Fechas_1981', 'Fechas_1982', 'Fechas_1983', 'Fechas_1984', 'Fechas_1985', 'Fechas_1986', 'Fechas_1987', 'Fechas_1988', 'Fechas_1989',
                                     'Fechas_1990', 'Fechas_1991', 'Fechas_1992', 'Fechas_1993', 'Fechas_1994', 'Fechas_1995', 'Fechas_1996', 'Fechas_1997', 'Fechas_1998',
                                     'Fechas_1999', 'Fechas_2000', 'Fechas_2001', 'Fechas_2002', 'Fechas_2003', 'Fechas_2004', 'Fechas_2005', 'Fechas_2006',
                                     'Fechas_2007', 'Fechas_2008', 'Fechas_2009', 'Fechas_2010', 'Fechas_2011', 'Fechas_2012', 'Fechas_2013', 'Fechas_2014',
                                    'Fechas_2015', 'Fechas_2016', 'Fechas_2017', 'Fechas_2018']
        
        
        df2 = pd.DataFrame(columns=f2,data=[[*[0]*len(f2)]])

        df2['Bcpp'] = self.Bcpp
        df2['Potencia'] = self.Potencia
        df2['Cilindraje'] = self.Cilindraje
        df2['PesoCategoria'] = self.PesoCategoria

        
        columM = [x for x in df2.columns if "Marca_" in x and str(self.Marca) == x.split('_')[-1]]
        df2[columM] = 1
        columC = [x for x in df2.columns if "Clase_" in x and str(self.Clase) == x.split('_')[-1]]
        df2[columC] = 1
        columF = [x for x in df2.columns if "Fechas_" in x and str(self.Fechas) == x.split('_')[-1]]
        df2[columF] = 1
        # Ese * en *salary_levels[self.salary_level] hace unpacking a la lista.
        # Sería como escribir salary_levels[self.salary_level][0], salary_levels[self.salary_level][1]
        return df2

    def predict(self, y_name: str = 'precio'):
        '''
        Clase para predecir.
        Carga el modelo, prepara los datos y predice.

        prediction = pd.DataFrame(self.model.predict(X)).rename(columns={0:y_name})

        '''
        self._load_model()
        X = self._prepare_data()
        prediction = pd.DataFrame(self.model.predict(X)).rename(columns={0: y_name})
        return prediction.to_dict(orient='records')