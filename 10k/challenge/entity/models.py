from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
#Model - Entity - str
class Entity(models.Model):

	name = models.CharField(max_length =200)
	symbol = models.CharField(max_length =200)
	documentType = models.CharField(max_length =200)
	CIK = models.CharField(max_length =200)

	amendmentFlat1 = models.CharField(max_length =200)
	amendmentFlat2 = models.CharField(max_length =200)
	amendmentFlat3 = models.CharField(max_length =200)

	documentFiscalPeriodEndDate1 = models.CharField(max_length =200)
	documentFiscalPeriodEndDate2 = models.CharField(max_length =200)
	documentFiscalPeriodEndDate3 = models.CharField(max_length =200)
	

	documentFiscalPeriodFocus1 = models.CharField(max_length =200)
	documentFiscalPeriodFocus2 = models.CharField(max_length =200)
	documentFiscalPeriodFocus3 = models.CharField(max_length =200)


	currentFiscalYearEndDate1 = models.CharField(max_length =200)
	currentFiscalYearEndDate2 = models.CharField(max_length =200)
	currentFiscalYearEndDate3 = models.CharField(max_length =200)
	
	seasonedIssuer1 = models.CharField(max_length =200)
	seasonedIssuer2 = models.CharField(max_length =200)
	seasonedIssuer3 = models.CharField(max_length =200)

	currentReportingStatus1 = models.CharField(max_length =200)
	currentReportingStatus2 = models.CharField(max_length =200)
	currentReportingStatus3 = models.CharField(max_length =200)

	voluntaryFilers1 = models.CharField(max_length =200)
	voluntaryFilers2 = models.CharField(max_length =200)
	voluntaryFilers3 = models.CharField(max_length =200)
	
	filerCategory1 = models.CharField(max_length =200)
	filerCategory2 = models.CharField(max_length =200)
	filerCategory3 = models.CharField(max_length =200)
	

	commonStockShareOutstanding1 = models.CharField(max_length =200)
	commonStockShareOutstanding2 = models.CharField(max_length =200)
	commonStockShareOutstanding3 = models.CharField(max_length =200)


	def publish (self):
		self.save()

	def __str__(self):
		return self.name