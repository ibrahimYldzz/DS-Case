# DS Case çalışması
Bu case çalışmasının amacı, verilen verisetine göre kredi sonucu tahmini yapabilen bir makine öğrenmesi modeli geliştirmek ve bunu production ortamında bir api şeklinde sunmaktır.

Yazılan api, Python ve Flask kullanılarak hazırlanmıştır. Daha sonrasında Dockerfile ile bir imaj hazırlanıp production ortamında kullanılmaya hazır hale getirilmiştir.








## Özellikler

- Dockerfile: Hazırlanan dockerfile sayesinde imaj ayağı kaldırılabilen ortamlarda api versiyon ve ortam bağımsız çalışabilmektedir.
- Model Başarısı: Hazırlanan kredi sonucu tahminleme modelinde %98 üzerinde bir başarı sağlanmıştır.



## API Kullanımı

#### Analitik hesaplama sonuçlarını getir

```http
  GET /is_alivee

  (Bu request api'ye healtcheck sorgusu yapabileceğimi get requestidir.)

```


```http
  POST /is_approval

  (Kredi tahminlemesi yapabileceğimiz post requestidir)

  Örnek request body:
  {
    "no_of_dependents": 5,
    "education": 0, 
    "self_employed": 0,	
    "income_annum": 4600000,	
    "loan_amount": 14400000, 
    "loan_term": 6, 
    "cibil_score": 785,
    "residential_assets_value": 650000, 
    "commercial_assets_value": 6300000, 
    "luxury_assets_value": 14700000, 
    "bank_asset_value": 6200000
    }

```



  
## Dağıtım

Bu projede imaj build etmek ve çalıştırmak için aşağıdaki komutları kullanabilirsiniz.

```bash
  docker image build -t case:1.0.0 .
```

```bash
  docker run -p 8080:8080 case:1.1.0
```

## Bilgisayarınızda Çalıştırın

Projeyi klonlayın

```bash
  git clone https://github.com/ibrahimYldzz/DS-Case.git
```

Proje dizinine gidin

```bash
  cd DS-Case
```

Gerekli paketleri yükleyin

```bash
  python -m venv env
  source env/bin/activate
  pip install -r requirements.txt
```

```bash
  gunicorn --config gunicorn_config.py app:app
```

  