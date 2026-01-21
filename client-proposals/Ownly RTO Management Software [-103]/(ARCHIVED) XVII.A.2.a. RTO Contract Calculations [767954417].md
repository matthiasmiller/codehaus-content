17.1.2.1. RTO Contract Calculations

Contract Types:

3 Standard Contracts:

  * Standard Contract
  * Standard Contract (Zero Down)
  * Standard Contract (90 Days Same as Cash)



1 CRA: by Cash Received

  * CRA by Cash Received



  


NOTE: In Ownly, divisor is auto-calculated based on Term Length and Cash Price %, rather than being selected by the user.

  


SORTO Standard Security Deposit (SORTO_Std_SecurityDeposit):

  * The standard RTO security deposit is editable until Calculate RTO is checked. At that point, if increased security deposits are now allowed and the current deposit it is greater than the default deposit, it is set to the default security deposit [see below].



Default Security Deposit: SoSubtotal / RTO Rate Divisor

  


  


Calculate RTO (SOCalculateRTO) sets the following fields ("SO" stands for corresponding Sales Order main screen field; "Breakdown" is the corresponding value from RTOGenerateBreakdown):

  * Subtotal = SOSubtotal
  * RTO Shipping = SOShipping
  * RTO Shipping is Taxable = SOShippingIsTaxable
  * RTO Tax Rate = SOEffectiveTaxRate
  * Rate Divisor = RTO Rate Divisor (RTOTermsDivisor)
  * Financing Base = Breakdown
  * Monthly Subtotal = Breakdown
  * Monthly Tax = Breakdown
  * Monthly Damage Waiver Fee = Breakdown
  * Monthly Payment = Breakdown
  * Security Deposit = Breakdown
  * CRA = Breakdown
  * Shipping Tax = Breakdown
  * Cash Due = Breakdown
  * Contract Contents = evaluated memo for RTO contract template



  


  


Niccolas Miller 07/23/2025: DONE_DB: Will we store shipping rates in Silverloom settings? Duane Burkholder 07/23/2025: DONE_NM: I don't understand the question. It might be something we can look at on tomorrows call.

Niccolas Miller 07/24/2025: Sure. Assist stores shipping details, such as Free Shipping Miles, $ / linear ft / mile, etc. in Silverloom Settings. I am wondering where we will get our shipping amounts.

  


TODO_DEV: Required pieces:

[X] Subtotal = cached field, set from Contract Entry

[X] Shipping = cached on contract

[X] Shipping is Taxable

[ ] Tax Rate = cached on contract record; auto-updated TODO_ Editability?

[X] Rate Divisor = cached when Contract Def is set

[X] DWF = cached as above

[X] Sec Deposit = Subtotal / RTORateDivisor (set when Contract Def is set, not editable on Contract record)

[X] CRA Cash Due - fielded on the ContDef record 

[X] Allow DWF and Allow Sec Deposit: cached on contract

  


Breakdown values:

RTOGenerateBreakdown( SORTOContractType

                    , SORTOSubtotal

                    , SORTOShipping

                    , SORTOShippingIsTaxable

                    , SORTOTaxRate

                    , SORTORateDivisor

                    , SORTODamageWaiverFee

                    , SORTO_Std_SecurityDeposit

                    , SORTO_CRA1_CashDue

                    , SORTO_CRA2_MonthlyPayment

                    , RTOContractField( SORTOContractTemplate, RTOContractDisallowDamageWaiverFee)

                    , RTOContractField( SORTOContractTemplate, RTOContractDisallowSecurityDeposit)

                    )

  


  


Financing Base

  * The financing base for a standard contract is simply the SO Subtotal.
  * The financing base for a CRA1 contract (cash received) is Subtotal - CRA Amount.
    * CRA Amount (cash received)*
      * = CashDue - Shipping - Tax - Subtotal / (TaxAdjustedRTORate - MonthlyDWF) * TaxAdjustedRTORate / ( TaxAdjustedRTORate - 1)
        * TaxAdjustedRTORate = RTORateDivisor / Sum( 1, (RTOTaxRate / 100))
        * RTOShippingTax = Shipping * (TaxRate / 100)
        * RTOTaxAdjustedRTORate( vRTORateDivisorFB, vTaxRateFB) = vRTORateDivisor / (1 + TaxRate/100)
          * Adjusted RTO Rate = RTORateDivisor / 1.08 [where tax rate is 8%]
            * RTORate is RTO Terms Divisor



  


Monthly Subtotal = FinancingBase / RTORateDivisor

  * [RTO_Std&StdZ&CRA1_PaymentSubtotal]: FinancingBase / RTORateDivisor



  


Total Monthly Payment

  * = Sum( Monthly Subtotal, Tax [Subtotal * Tax Rate], DWF)



  


Monthly Tax = Subtotal * Tax Rate

  


Security Deposit (only for standard contracts) = If( SOSecDeposit is NA, Financing Base / RTORateDivisor, SOSecDeposit)

  * RTO_Std&StdZ_SecurityDeposit: Financing Base / RTORateDivisor



  


CRA Amount (same as above)*

  


Cash Due

  * Standard Contract (Zero Down/Standard): Total Monthly Payment + Security Deposit + Shipping + Shipping Tax
  * Standard Contract (90 Days Same as Cash): 0
  * CRA: Total Monthly Payment + CRA Amount + Shipping + Shipping Tax


