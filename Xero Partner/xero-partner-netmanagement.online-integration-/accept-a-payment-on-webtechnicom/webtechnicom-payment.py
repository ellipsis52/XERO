/bin/sh /Users/netmanagement/Downloads/braintree_node-master/node_modules/braintree/webtechnicom\ paypal\ payement\ gateway/accept-a-payment-on-webtechnicom/.conda/bin/xzmore
(.venv) (base) netmanagement@iMac-de-steve bin % /bin/sh /Users/netmanagement/Downloads/braintree_node-master/node_modules/braintree/webtechnicom\ paypal\ payement\ gateway/accept-a-payment-on-webtechnicom/.conda/bin/xzmore
Usage: xzmore [OPTION]... [FILE]...
Like 'more', but operate on the uncompressed contents of xz compressed FILEs.

Report bugs to <xz@tukaani.org>.
(.venv) (base) netmanagement@iMac-de-steve bin % /bin/sh /Users/netmanagement/Downloads/braintree_node-master/node_modules/braintree/webtechnicom\ paypal\ payement\ gateway/accept-a-payment-on-webtechnicom/.conda/bin/xzmore
Usage: xzmore [OPTION]... [FILE]...
Like 'more', but operate on the uncompressed contents of xz compressed FILEs.

Report bugs to <xz@tukaani.org>.
(.venv) (base) netmanagement@iMac-de-steve bin % /bin/sh /Users/netmanagement/Downloads/braintree_node-master/node_modules/braintree/webtechnicom\ paypal\ payement\ gateway/accept-a-payment-on-webtechnicom/.conda/bin/xzmore
Usage: xzmore [OPTION]... [FILE]...
Like 'more', but operate on the uncompressed contents of xz compressed FILEs.

Report bugs to <xz@tukaani.org>.
(.venv) (base) netmanagement@iMac-de-steve bin % /bin/sh /Users/netmanagement/Downloads/braintree_node-master/node_modules/braintree/webtechnicom\ paypal\ payement\ gateway/accept-a-payment-on-webtechnicom/.conda/bin/xzcmp
/Users/netmanagement/Downloads/braintree_node-master/node_modules/braintree/webtechnicom paypal payement gateway/accept-a-payment-on-webtechnicom/.conda/bin/xzcmp: Invalid number of operands; try `xzcmp --help' for help
(.venv) (base) netmanagement@iMac-de-steve bin % >....
--------------------

Documentation for the python bindings can be found alongside Stripe's other bindings here:

- https://stripe.com/docs
- https://stripe.com/docs/api/?lang=python

In the standard documentation (the first link), most of the reference pages will have examples in Stripe's official bindings (including Python). Just click on the Python tab to get the relevant documentation.

In the full API reference for python (the second link), the right half of the page will provide example requests and responses for various API calls.

quote> >....
stripe/treasury/_received_credit.py,sha256=tbbUw5Gc5idXGvNaySu0EC0VTB8lkBdjs8PUx6a_4p8,18543
stripe/treasury/_received_credit_service.py,sha256=pZyu3zIVPxfUAZP3aoIhN2ESsKJeLBz_Zy6YkGY6OTU,4891
stripe/treasury/_received_debit.py,sha256=XafFm93mGZmYUMu4a4yvOk6_39jAAohmJWYvpdseEL8,16029
stripe/treasury/_received_debit_service.py,sha256=ZglvGaLNtBEvukBSSbdCTOUTpfD5zOx_wDHSvAlutkM,4390
stripe/treasury/_transaction.py,sha256=saWUDXyiqnOIEgsGHFmKZKvKhxOmRtWGcfdCLm18a_w,12901
stripe/treasury/_transaction_entry.py,sha256=iKPLOzd5SLmQBxghDiNzP8DbpAeKtFKwx1KYSgKk6X4,12760
stripe/treasury/_transaction_entry_service.py,sha256=zUHkyrbGRkkey9DEOEEPEpARi2-oZbLDaK9ldnjkY70,5752
stripe/treasury/_transaction_service.py,sha256=JAdUe2V30EggdvMH7GEy2jwzLlJ5_4WOLE5fIYwLl8g,6072
stripe/util.py,sha256=vjZ9XlpSir5bD9rTjDHUuycF5zSwr3OWtT0_J47v0xg,453
stripe/version.py,sha256=pXbS7TKI7G3x3pETXNxL1y-Pvo8kB80_9LSO-OtsVXI,368
stripe/webhook.py,sha256=CXf9H3r6K9TO7WjYNIx8MuGDUCE4E8-cubJVgtNLK_E,477

quote> Wheel-Version: 1.0
Generator: bdist_wheel (0.43.0)
Root-Is-Purelib: true
Tag: py2-none-any
Tag: py3-none-any


quote> >....
if not TYPE_CHECKING:
    from stripe.api_resources.billing.alert import Alert
    from stripe.api_resources.billing.alert_triggered import AlertTriggered
    from stripe.api_resources.billing.meter import Meter
    from stripe.api_resources.billing.meter_event import MeterEvent
    from stripe.api_resources.billing.meter_event_adjustment import (
        MeterEventAdjustment,
    )
    from stripe.api_resources.billing.meter_event_summary import (
        MeterEventSummary,
    )

quote> >....
      from stripe.api_resources.billing.alert import Alert
    To:
      from stripe.billing import Alert
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.billing._alert import (  # noqa
        Alert,
    )

quote> >....                                                                                                                                                      
      from stripe.api_resources.billing.alert_triggered import AlertTriggered
    To:
      from stripe.billing import AlertTriggered
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.billing._alert_triggered import (  # noqa
        AlertTriggered,
    )

quote> >....
      from stripe.api_resources.billing.meter import Meter
    To:
      from stripe.billing import Meter
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.billing._meter import (  # noqa
        Meter,
    )

quote> >....                                                                                                                                                      
      from stripe.api_resources.billing.meter_event import MeterEvent
    To:
      from stripe.billing import MeterEvent
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.billing._meter_event import (  # noqa
        MeterEvent,
    )

quote> >....
      from stripe.api_resources.billing.meter_event_adjustment import MeterEventAdjustment
    To:
      from stripe.billing import MeterEventAdjustment
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.billing._meter_event_adjustment import (  # noqa
        MeterEventAdjustment,
    )

quote> >....                                                                                                                                                      
      from stripe.api_resources.billing.meter_event_summary import MeterEventSummary
    To:
      from stripe.billing import MeterEventSummary
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.billing._meter_event_summary import (  # noqa
        MeterEventSummary,
    )

quote> >....
    From:
      from stripe.api_resources.billing_portal import ...
    To:
      from stripe.billing_portal import ...
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.api_resources.billing_portal.configuration import Configuration
    from stripe.api_resources.billing_portal.session import Session

quote> >....                                                                                                                                                      
      from stripe.api_resources.billing_portal.configuration import Configuration
    To:
      from stripe.billing_portal import Configuration
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.billing_portal._configuration import (  # noqa
        Configuration,
    )

quote> >....
      from stripe.api_resources.billing_portal.session import Session
    To:
      from stripe.billing_portal import Session
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.billing_portal._session import (  # noqa
        Session,
    )

quote> >....                                                                                                                                                      
    imports to import from stripe.checkout directly.
    From:
      from stripe.api_resources.checkout import ...
    To:
      from stripe.checkout import ...
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.api_resources.checkout.session import Session
¨
quote> >....
      from stripe.api_resources.checkout.session import Session
    To:
      from stripe.checkout import Session
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.checkout._session import (  # noqa
        Session,
    )

quote> >....                                                                                                                                                      
    )
    from stripe.api_resources.financial_connections.account_ownership import (
        AccountOwnership,
    )
    from stripe.api_resources.financial_connections.institution import (
        Institution,
    )
    from stripe.api_resources.financial_connections.session import Session
    from stripe.api_resources.financial_connections.transaction import (
        Transaction,
    )

quote> >....                                                                                                                                                      
      from stripe.api_resources.financial_connections.account import Account
    To:
      from stripe.financial_connections import Account
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.financial_connections._account import (  # noqa
        Account,
    )

quote> >....
      from stripe.api_resources.financial_connections.account_inferred_balance import AccountInferredBalance
    To:
      from stripe.financial_connections import AccountInferredBalance
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.financial_connections._account_inferred_balance import (  # noqa
        AccountInferredBalance,
    )

quote> >....                                                                                                                                                      
      from stripe.api_resources.financial_connections.account_inferred_balance import AccountInferredBalance
    To:
      from stripe.financial_connections import AccountInferredBalance
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.financial_connections._account_inferred_balance import (  # noqa
        AccountInferredBalance,
    )

quote> >....
      from stripe.api_resources.financial_connections.transaction import Transaction
    To:
      from stripe.financial_connections import Transaction
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.financial_connections._transaction import (  # noqa
        Transaction,
    )

quote> >....                                                                                                                                                      
#   - RecipientTransfer is a manually maintained deprecated class
if not TYPE_CHECKING:
    from stripe.api_resources.error_object import ErrorObject
    from stripe.api_resources.error_object import (
        OAuthErrorObject,
    )
    from stripe.api_resources.file import (
        File as FileUpload,
    )

    from stripe.api_resources.recipient_transfer import RecipientTransfer

if> >....                                                                                                                                                         
      from stripe.api_resources.account import Account
    To:
      from stripe import Account
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._account import (  # noqa
        Account,
    )

if if> >....
      from stripe.api_resources.account_link import AccountLink
    To:
      from stripe import AccountLink
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._account_link import (  # noqa
        AccountLink,
    )

if if if> >....                                                                                                                                                   
      from stripe.api_resources.apple_pay_domain import ApplePayDomain
    To:
      from stripe import ApplePayDomain
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._apple_pay_domain import (  # noqa
        ApplePayDomain,
    )

if if if if if if> >....
      from stripe.api_resources.application_fee import ApplicationFee
    To:
      from stripe import ApplicationFee
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._application_fee import (  # noqa
        ApplicationFee,
    )

if if if if if if if if> >....                                                                                                                                    
      from stripe.api_resources.balance_transaction import BalanceTransaction
    To:
      from stripe import BalanceTransaction
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._balance_transaction import (  # noqa
        BalanceTransaction,
    )

if if if if if if if if if if if> >....
      from stripe.api_resources.bank_account import BankAccount
    To:
      from stripe import BankAccount
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._bank_account import (  # noqa
        BankAccount,
    )

if if if if if if if if if if if if> >....                                                                                                                        
      from stripe.api_resources.capability import Capability
    To:
      from stripe import Capability
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._capability import (  # noqa
        Capability,
    )

if if if if if if if if if if if if if> >....
      from stripe.api_resources.card import Card
    To:
      from stripe import Card
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._card import (  # noqa
        Card,
    )

if if if if if if if if if if if if if if> >....                                                                                                                  
      from stripe.api_resources.cash_balance import CashBalance
    To:
      from stripe import CashBalance
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._cash_balance import (  # noqa
        CashBalance,
    )

if if if if if if if if if if if if if if if> >....
      from stripe.api_resources.charge import Charge
    To:
      from stripe import Charge
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._charge import (  # noqa
        Charge,
    )

if if if if if if if if if if if if if if if if> >....                                                                                                            
      from stripe.api_resources.confirmation_token import ConfirmationToken
    To:
      from stripe import ConfirmationToken
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._confirmation_token import (  # noqa
        ConfirmationToken,
    )

if if if if if if if if if if if if if if if if if> >....
      from stripe.api_resources.connect_collection_transfer import ConnectCollectionTransfer
    To:
      from stripe import ConnectCollectionTransfer
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._connect_collection_transfer import (  # noqa
        ConnectCollectionTransfer,
    )

if if if if if if if if if if if if if if if if if if> >....                                                                                                      
      from stripe.api_resources.country_spec import CountrySpec
    To:
      from stripe import CountrySpec
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._country_spec import (  # noqa
        CountrySpec,
    )

if if if if if if if if if if if if if if if if if if if> >....
      from stripe.api_resources.coupon import Coupon
    To:
      from stripe import Coupon
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._coupon import (  # noqa
        Coupon,
    )

if if if if if if if if if if if if if if if if if if if if> >....                                                                                                
      from stripe.api_resources.credit_note import CreditNote
    To:
      from stripe import CreditNote
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._credit_note import (  # noqa
        CreditNote,
    )

if if if if if if if if if if if if if if if if if if if if if> >....
      from stripe.api_resources.credit_note_line_item import CreditNoteLineItem
    To:
      from stripe import CreditNoteLineItem
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._credit_note_line_item import (  # noqa
        CreditNoteLineItem,
    )

if if if if if if if if if if if if if if if if if if if if if if> >....                                                                                          
      from stripe.api_resources.customer import Customer
    To:
      from stripe import Customer
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._customer import (  # noqa
        Customer,
    )

if if if if if if if if if if if if if if if if if if if if if if if> >....
      from stripe.api_resources.customer import Customer
    To:
      from stripe import Customer
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._customer import (  # noqa
        Customer,
    )

if if if if if if if if if if if if if if if if if if if if if if if if> >....                                                                                    
      from stripe.api_resources.customer_cash_balance_transaction import CustomerCashBalanceTransaction
    To:
      from stripe import CustomerCashBalanceTransaction
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._customer_cash_balance_transaction import (  # noqa
        CustomerCashBalanceTransaction,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if> >....
      from stripe.api_resources.customer_session import CustomerSession
    To:
      from stripe import CustomerSession
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._customer_session import (  # noqa
        CustomerSession,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if> >....                                                                              
      from stripe.api_resources.dispute import Dispute
    To:
      from stripe import Dispute
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._dispute import (  # noqa
        Dispute,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....
      from stripe.api_resources.error_object import ErrorObject
    To:
      from stripe import ErrorObject
    """,
    DeprecationWarning,
)
if not TYPE_CHECKING:
    from stripe._error_object import (  # noqa
        ErrorObject,
        OAuthErrorObject,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....                                                                  
      from stripe.api_resources.exchange_rate import ExchangeRate
    To:
      from stripe import ExchangeRate
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._exchange_rate import (  # noqa
        ExchangeRate,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....
      from stripe.api_resources.file import File
    To:
      from stripe import File
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._file import (  # noqa
        File,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....                                                         
      from stripe.api_resources.file_link import FileLink
    To:
      from stripe import FileLink
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._file_link import (  # noqa
        FileLink,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....
      from stripe.api_resources.file_link import FileLink
    To:
      from stripe import FileLink
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._file_link import (  # noqa
        FileLink,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....                                                   
      from stripe.api_resources.funding_instructions import FundingInstructions
    To:
      from stripe import FundingInstructions
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._funding_instructions import (  # noqa
        FundingInstructions,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....
      from stripe.api_resources.invoice import Invoice
    To:
      from stripe import Invoice
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._invoice import (  # noqa
        Invoice,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....                                             
      from stripe.api_resources.invoice_line_item import InvoiceLineItem
    To:
      from stripe import InvoiceLineItem
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._invoice_line_item import (  # noqa
        InvoiceLineItem,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....
      from stripe.api_resources.line_item import LineItem
    To:
      from stripe import LineItem
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._line_item import (  # noqa
        LineItem,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....                                 
      from stripe.api_resources.list_object import ListObject
    To:
      from stripe import ListObject
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._list_object import (  # noqa
        ListObject,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....
      from stripe.api_resources.login_link import LoginLink
    To:
      from stripe import LoginLink
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._login_link import (  # noqa
        LoginLink,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....                           
      from stripe.api_resources.mandate import Mandate
    To:
      from stripe import Mandate
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._mandate import (  # noqa
        Mandate,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....
      from stripe.api_resources.order import Order
    To:
      from stripe import Order
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._order import (  # noqa
        Order,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....                  
      from stripe.api_resources.payment_link import PaymentLink
    To:
      from stripe import PaymentLink
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._payment_link import (  # noqa
        PaymentLink,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....
      from stripe.api_resources.payout import Payout
    To:
      from stripe import Payout
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._payout import (  # noqa               
        Payout,                    
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >.
      from stripe.api_resources.person import Person
    To:
      from stripe import Person
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._person import (  # noqa
        Person,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....
      from stripe.api_resources.plan import Plan
    To:
      from stripe import Plan
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._plan import (  # noqa
        Plan,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....                                                                                                                                                         
      from stripe.api_resources.product import Product
    To:
      from stripe import Product
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._product import (  # noqa
        Product,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....
      from stripe.api_resources.product_feature import ProductFeature
    To:
      from stripe import ProductFeature
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._product_feature import (  # noqa
        ProductFeature,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....                                                                                                                                                
      from stripe.api_resources.promotion_code import PromotionCode
    To:
      from stripe import PromotionCode
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._promotion_code import (  # noqa
        PromotionCode,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....
      from stripe.api_resources.quote_preview_subscription_schedule import QuotePreviewSubscriptionSchedule
    To:
      from stripe import QuotePreviewSubscriptionSchedule
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._quote_preview_subscription_schedule import (  # noqa
        QuotePreviewSubscriptionSchedule,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....                                                                                                                              
      from stripe.api_resources.setup_attempt import SetupAttempt             
    To:
      from stripe import SetupAttempt      
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._setup_attempt import (  # noqa
        SetupAttempt,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....
      from stripe.api_resources.source import Source
    To:
      from stripe import Source
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._source import (  # noqa       
        Source,      
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....                                                                                                   
      from stripe.api_resources.subscription_item import SubscriptionItem  
    To:
      from stripe import SubscriptionItem 
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._subscription_item import (  # noqa
        SubscriptionItem,
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....
      from stripe.api_resources.tax_rate import TaxRate
    To:
      from stripe import TaxRate
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._tax_rate import (  # noqa              
        TaxRate,            
    )

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....                                                                        
    DeprecationWarning,                                                       
    stacklevel=2,
)                                          
if not TYPE_CHECKING:
    from stripe._webhook_endpoint import (  # noqa
        WebhookEndpoint,
    )
# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec                
from stripe.apps._secret import Secret as Secret
from stripe.apps._secret_service import SecretService as SecretService

if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if> >....                                                      
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    _inner_class_types = {"scope": Scope}

zsh: parse error near `)'
(.venv) (base) netmanagement@iMac-de-steve bin % >....                                                                                                            
        return cast(
            Secret,
            await self._request_async(
                "post",
                "/v1/apps/secrets/delete",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

zsh: no matches found: -*-
zsh: command not found: #
zsh: command not found: from
zsh: command not found: from
zsh: command not found: from
zsh: command not found: from
zsh: command not found: from
zsh: command not found: from
zsh: no matches found: SecretService(StripeService):
zsh: no matches found: CreateParams(TypedDict):
zsh: no matches found: NotRequired[List[str]]
zsh: command not found: \n        Specifies which fields in the response should be expanded.\n        
zsh: no matches found: NotRequired[int]
zsh: command not found: \n        The Unix timestamp for the expiry time of the secret, after which the secret deletes.\n        
zsh: command not found: name:
zsh: command not found: \n        A name for the secret that's unique within the scope.\n        
zsh: command not found: payload:
zsh: command not found: \n        The plaintext secret value to be stored.\n        
zsh: command not found: scope:
zsh: command not found: \n        Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.\n        
zsh: no matches found: CreateParamsScope(TypedDict):
zsh: bad pattern: Literal[account,
zsh: command not found: \n        The secret scope type.\n        
zsh: no matches found: NotRequired[str]
zsh: command not found: user
zsh: command not found: account
zsh: command not found: \n        The user ID. This field is required if  is set to , and should not be provided if  is set to .\n        
zsh: no matches found: DeleteWhereParams(TypedDict):
zsh: no matches found: NotRequired[List[str]]
zsh: command not found: \n        Specifies which fields in the response should be expanded.\n        
zsh: command not found: name:
zsh: command not found: \n        A name for the secret that's unique within the scope.\n        
zsh: command not found: scope:
zsh: command not found: \n        Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.\n        
zsh: no matches found: DeleteWhereParamsScope(TypedDict):
zsh: bad pattern: Literal[account,
zsh: command not found: \n        The secret scope type.\n        
zsh: no matches found: NotRequired[str]
zsh: command not found: user
zsh: command not found: account
zsh: command not found: \n        The user ID. This field is required if  is set to , and should not be provided if  is set to .\n        
zsh: no matches found: FindParams(TypedDict):
zsh: no matches found: NotRequired[List[str]]
zsh: command not found: \n        Specifies which fields in the response should be expanded.\n        
zsh: command not found: name:
zsh: command not found: \n        A name for the secret that's unique within the scope.\n        
zsh: command not found: scope:
zsh: command not found: \n        Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.\n        
zsh: no matches found: FindParamsScope(TypedDict):
zsh: bad pattern: Literal[account,
zsh: command not found: \n        The secret scope type.\n        
zsh: no matches found: NotRequired[str]
zsh: command not found: user
zsh: command not found: account
zsh: command not found: \n        The user ID. This field is required if  is set to , and should not be provided if  is set to .\n        
zsh: no matches found: ListParams(TypedDict):
zsh: no matches found: NotRequired[str]
zsh: command not found: ending_before
zsh: command not found: obj_bar
zsh: file name too long: \n        A cursor for use in pagination.  is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with , your subsequent call can include  in order to fetch the previous page of the list.\n        
zsh: no matches found: NotRequired[List[str]]
zsh: command not found: \n        Specifies which fields in the response should be expanded.\n        
zsh: no matches found: NotRequired[int]
zsh: command not found: \n        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.\n        
zsh: command not found: scope:
zsh: command not found: \n        Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.\n        
zsh: no matches found: NotRequired[str]
zsh: command not found: starting_after
zsh: command not found: obj_foo
zsh: file name too long: \n        A cursor for use in pagination.  is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with , your subsequent call can include  in order to fetch the next page of the list.\n        
zsh: no matches found: ListParamsScope(TypedDict):
zsh: bad pattern: Literal[account,
zsh: command not found: \n        The secret scope type.\n        
zsh: no matches found: NotRequired[str]
zsh: command not found: user
zsh: command not found: account
zsh: command not found: \n        The user ID. This field is required if  is set to , and should not be provided if  is set to .\n        
zsh: unknown file attribute: \n
zsh: command not found: \n        List all secrets stored on the given scope.\n        
zsh: bad pattern: cast(\n            ListObject[Secret],\n            self._request(\n                get,\n                /v1/apps/secrets,\n                api_mode=V1,\n                base_address=api,\n                params=params,\n                options=options,\n            ),\n        )
(.venv) (base) netmanagement@iMac-de-steve bin % # -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.billing_portal._configuration import Configuration as Configuration
from stripe.billing_portal._configuration_service import (
    ConfigurationService as ConfigurationService,
)
from stripe.billing_portal._session import Session as Session
from stripe.billing_portal._session_service import (
    SessionService as SessionService,
)

zsh: no matches found: -*-
zsh: command not found: #
zsh: command not found: from
zsh: unknown file attribute: \n
zsh: command not found: from
zsh: unknown file attribute: \n
(.venv) (base) netmanagement@iMac-de-steve bin % >....                                                                                                            
        return cast(   
            Session,                                                       
            await self._request_async(                 
                "post",
                "/v1/billing_portal/sessions",
                api_mode="V1",     
                base_address="api",
                params=params,  
                options=options,
            ),                         
        )

zsh: parse error near `}'
(.venv) (base) netmanagement@iMac-de-steve bin % >....                                                                                                            
)
from stripe.billing._meter_event_service import (
    MeterEventService as MeterEventService,
)
from stripe.billing._meter_event_summary import (
    MeterEventSummary as MeterEventSummary,
)
from stripe.billing._meter_event_summary_service import (
    MeterEventSummaryService as MeterEventSummaryService,
)
from stripe.billing._meter_service import MeterService as MeterService

zsh: no matches found: -*-
zsh: command not found: #
zsh: command not found: from
zsh: command not found: from
zsh: command not found: from
zsh: command not found: from
zsh: command not found: from
zsh: unknown file attribute: \n
zsh: unknown file attribute: \n
zsh: unknown file attribute: \n
zsh: unknown file attribute: \n
zsh: unknown file attribute: \n
zsh: command not found: from
(.venv) (base) netmanagement@iMac-de-steve bin % >....                                                                                                            
        """
        Retrieves a billing alert given an ID
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {
        "filter": Filter,
        "usage_threshold_config": UsageThresholdConfig,
    }

zsh: parse error near `)'
(.venv) (base) netmanagement@iMac-de-steve bin % >....                                                                                                            
                ),
                params=params,                                                                                    
            ),
        )                                     

    _inner_class_types = {                                                               
        "customer_mapping": CustomerMapping,
        "default_aggregation": DefaultAggregation,
        "status_transitions": StatusTransitions,
        "value_settings": ValueSettings,
    }  

zsh: parse error near `)'
(.venv) (base) netmanagement@iMac-de-steve bin % >....                                                                                                            
        """
        Creates a billing meter event
        """
        return cast(
            "MeterEvent",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

zsh: parse error near `)'
(.venv) (base) netmanagement@iMac-de-steve bin % >....                                                                                                            
        """
        return cast(
            "MeterEventAdjustment",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    _inner_class_types = {"cancel": Cancel}

zsh: parse error near `)'
(.venv) (base) netmanagement@iMac-de-steve bin % >....
        return cast(
            MeterEventAdjustment,
            await self._request_async(
                "post",
                "/v1/billing/meter_event_adjustments",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

zsh: no matches found: -*-
zsh: command not found: #
zsh: command not found: from
zsh: command not found: from
zsh: command not found: from
zsh: command not found: from
zsh: command not found: from
zsh: no matches found: MeterEventAdjustmentService(StripeService):
zsh: no matches found: CreateParams(TypedDict):
zsh: no matches found: NotRequired[MeterEventAdjustmentService.CreateParamsCancel]
zsh: command not found: \n        Specifies which event to cancel.\n
zsh: command not found: event_name:
zsh: command not found: event_name
zsh: command not found: \n        The name of the meter event. Corresponds with the  field on a meter.\n
zsh: no matches found: NotRequired[List[str]]
zsh: command not found: \n        Specifies which fields in the response should be expanded.\n
zsh: no matches found: Literal[cancel]
zsh: command not found: \n        Specifies whether to cancel a single event or a range of events for a time period. Time period cancellation is not supported yet.\n
zsh: no matches found: CreateParamsCancel(TypedDict):
zsh: no matches found: NotRequired[str]
zsh: command not found: \n        Unique identifier for the event. You can only cancel events within 24 hours of Stripe receiving them.\n
zsh: unknown file attribute: \n
zsh: command not found: \n        Creates a billing meter event adjustment\n
zsh: bad pattern: cast(\n            MeterEventAdjustment,\n            self._request(\n                post,\n                /v1/billing/meter_event_adjustments,\n                api_mode=V1,\n                base_address=api,\n                params=params,\n                options=options,\n            ),\n        )
(.venv) (base) netmanagement@iMac-de-steve bin % >....
        return cast(
            MeterEvent,
            await self._request_async(
                "post",
                "/v1/billing/meter_events",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

zsh: no matches found: -*-
zsh: command not found: #
zsh: command not found: from
zsh: command not found: from
zsh: command not found: from
zsh: command not found: from
zsh: command not found: from
zsh: no matches found: MeterEventService(StripeService):
zsh: no matches found: CreateParams(TypedDict):
zsh: command not found: event_name:
zsh: command not found: event_name
zsh: command not found: \n        The name of the meter event. Corresponds with the  field on a meter.\n
zsh: no matches found: NotRequired[List[str]]
zsh: command not found: \n        Specifies which fields in the response should be expanded.\n
zsh: no matches found: NotRequired[str]
zsh: command not found: \n        A unique identifier for the event. If not provided, one will be generated. We recommend using a globally unique identifier for this. We'll enforce uniqueness within a rolling 24 hour period.\n
zsh: bad pattern: Dict[str,
zsh: command not found: customer_mapping.event_payload_key
zsh: command not found: stripe_customer_id
zsh: command not found: value_settings.event_payload_key
zsh: command not found: value
zsh: no such file or directory: \n        The payload of the event. This must contain the fields corresponding to a meter's  (default is ) and  (default is ). Read more about the [payload](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage#payload-key-overrides).\n
zsh: no matches found: NotRequired[int]
zsh: command not found: \n        The time of the event. Measured in seconds since the Unix epoch. Must be within the past 35 calendar days or up to 5 minutes in the future. Defaults to current timestamp if not specified.\n
zsh: unknown file attribute: \n
zsh: command not found: \n        Creates a billing meter event\n
zsh: bad pattern: cast(\n            MeterEvent,\n            self._request(\n                post,\n                /v1/billing/meter_events,\n                api_mode=V1,\n                base_address=api,\n                params=params,\n                options=options,\n            ),\n        )
(.venv) (base) netmanagement@iMac-de-steve bin % >....
    """
    The meter associated with this event summary.
    """
    object: Literal["billing.meter_event_summary"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    start_time: int
    """
    Start timestamp for this event summary (inclusive). Must be aligned with minute boundaries.
    """

zsh: no matches found: -*-
zsh: command not found: #
zsh: command not found: from
zsh: command not found: from
zsh: command not found: from
zsh: no matches found: MeterEventSummary(StripeObject):
zsh: command not found: \n    A billing meter event summary represents an aggregated view of a customer's billing meter events within a specified timeframe. It indicates how much\n    usage was accrued by a customer for that period.\n
zsh: no matches found: ClassVar[Literal[billing.meter_event_summary]]
zsh: command not found: aggregated_value:
zsh: command not found: start_time
zsh: command not found: end_time
zsh: command not found: default_aggregation
zsh: command not found: \n    Aggregated value of all the events within  (inclusive) and  (inclusive). The aggregation strategy is defined on meter via .\n
zsh: command not found: end_time:
zsh: command not found: \n    End timestamp for this event summary (exclusive). Must be aligned with minute boundaries.\n
zsh: command not found: id:
zsh: command not found: \n    Unique identifier for the object.\n
zsh: command not found: livemode:
zsh: command not found: \n    Has the value  if the object exists in live mode or the value  if the object exists in test mode.\n
zsh: command not found: meter:
zsh: command not found: \n    The meter associated with this event summary.\n
zsh: no matches found: Literal[billing.meter_event_summary]
zsh: command not found: \n    String representing the object's type. Objects of the same type share the same value.\n
zsh: command not found: start_time:
zsh: command not found: \n    Start timestamp for this event summary (inclusive). Must be aligned with minute boundaries.\n
(.venv) (base) netmanagement@iMac-de-steve bin % >....
            await self._request_async(
                "get",
                "/v1/billing/meters/{id}/event_summaries".format(
                    id=sanitize_id(id),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

zsh: no matches found: -*-
zsh: command not found: #
zsh: command not found: from
zsh: command not found: from
zsh: command not found: from
zsh: command not found: from
zsh: command not found: from
zsh: command not found: from
zsh: command not found: from
zsh: no matches found: MeterEventSummaryService(StripeService):
zsh: no matches found: ListParams(TypedDict):
zsh: command not found: customer:
zsh: command not found: \n        The customer for which to fetch event summaries.\n
zsh: command not found: end_time:
zsh: command not found: \n        The timestamp from when to stop aggregating meter events (exclusive). Must be aligned with minute boundaries.\n
zsh: no matches found: NotRequired[str]
zsh: command not found: ending_before
zsh: command not found: obj_bar
zsh: file name too long: \n        A cursor for use in pagination.  is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with , your subsequent call can include  in order to fetch the previous page of the list.\n
zsh: no matches found: NotRequired[List[str]]
zsh: command not found: \n        Specifies which fields in the response should be expanded.\n
zsh: no matches found: NotRequired[int]
zsh: command not found: \n        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.\n
zsh: command not found: start_time:
zsh: command not found: \n        The timestamp from when to start aggregating meter events (inclusive). Must be aligned with minute boundaries.\n
zsh: no matches found: NotRequired[str]
zsh: command not found: starting_after
zsh: command not found: obj_foo
zsh: file name too long: \n        A cursor for use in pagination.  is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with , your subsequent call can include  in order to fetch the next page of the list.\n
zsh: bad pattern: NotRequired[Literal[day,
zsh: file name too long: \n        Specifies what granularity to use when generating event summaries. If not specified, a single event summary would be returned for the specified time range. For hourly granularity, start and end times must align with hour boundaries (e.g., 00:00, 01:00, ..., 23:00). For daily granularity, start and end times must align with UTC day boundaries (00:00 UTC).\n
zsh: unknown file attribute: \n
zsh: command not found: \n        Retrieve a list of billing meter event summaries.\n
zsh: bad pattern: cast(\n            ListObject[MeterEventSummary],\n            self._request(\n                get,\n                /v1/billing/meters/{id}/event_summaries.format(\n                    id=sanitize_id(id),\n                ),\n                api_mode=V1,\n                base_address=api,\n                params=params,\n                options=options,\n            ),\n        )
(.venv) (base) netmanagement@iMac-de-steve bin % >....
            await self._request_async(
                "post",
                "/v1/billing/meters/{id}/reactivate".format(
                    id=sanitize_id(id)
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

zsh: no matches found: -*-
zsh: command not found: #
zsh: command not found: from
zsh: command not found: from
zsh: command not found: from
zsh: command not found: from
zsh: command not found: from
zsh: unknown file attribute: \n
zsh: command not found: from
zsh: command not found: from
zsh: no matches found: MeterService(StripeService):
zsh: no matches found: __init__(self, requestor):
zsh: missing end of string
zsh: no matches found: CreateParams(TypedDict):
zsh: bad pattern: NotRequired[
zsh: command not found: MeterService.CreateParamsCustomerMapping
zsh: command not found: ]
zsh: command not found: \n        Fields that specify how to map a meter event to a customer.\n
zsh: command not found: default_aggregation:
zsh: command not found: \n        The default settings to aggregate a meter's events with.\n
zsh: command not found: display_name:
zsh: command not found: \n        The meter's name.\n
zsh: command not found: event_name:
zsh: command not found: event_name
zsh: command not found: \n        The name of the meter event to record usage for. Corresponds with the  field on meter events.\n
zsh: bad pattern: NotRequired[Literal[day,
zsh: command not found: \n        The time window to pre-aggregate meter events for, if any.\n
zsh: no matches found: NotRequired[List[str]]
zsh: command not found: \n        Specifies which fields in the response should be expanded.\n
zsh: no matches found: NotRequired[MeterService.CreateParamsValueSettings]
zsh: command not found: \n        Fields that specify how to calculate a meter event's value.\n
zsh: no matches found: CreateParamsCustomerMapping(TypedDict):
zsh: command not found: event_payload_key:
zsh: command not found: \n        The key in the usage event payload to use for mapping the event to a customer.\n
zsh: no matches found: Literal[by_id]
zsh: command not found: by_id
zsh: command not found: \n        The method for mapping a meter event to a customer. Must be .\n
zsh: no matches found: CreateParamsDefaultAggregation(TypedDict):
zsh: bad pattern: Literal[count,
zsh: command not found: count
stripe billing meter_events create  \
  --event-name=alpaca_ai_tokens \
  -d "payload[value]"=25 \
  -d "payload[stripe_customer_id]"={{CUSTOMER_ID}}
stripe billing meter_event_adjustments create  \
  --type=cancel \
  --event-name=alpaca_ai_tokens \
  -d "cancel[identifier]"={{METER_EVENT_IDENTIFIER}}
stripe billing meter_event_adjustments create  \
  --type=cancel \
  --event-name=ai_search_api \
  -d "cancel[identifier]"=identifier_123
{
  "object": "billing.meter_event_adjustment",
  "livemode": false,
  "status": "pending",
  "event_name": "ai_search_api",
  "type": "cancel",
  "cancel": {
    "identifier": "identifier_123"
  }
}
{
  "id": "mtrusg_test_6041CMAXJrFdZ56U76ce6L35Hz7xA3Tn58z5sY7bq6gM3XN5bx5Y459D4Xt2E17ko6M86kt7kV3bl5PM7LV59l4sY50b6oU5QD7bY3HP58z5sY7bq6gM3Y57LF2Dr7od3Hb8927gh4Tt4Lo4xO4ge60T81C6Y53gl4QS2D33ft3HC3Xi3Cy3Cy3Cy",
  "object": "billing.meter_event_summary",
  "aggregated_value": 10,
  "end_time": 1711659600,
  "livemode": false,
  "meter": "mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA",
  "start_time": 1711656000
}
stripe billing meter_event_summarys list mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA \
  --customer=cus_Pp40waj64hdRxb \
  --start-time=1711584000 \
  --end-time=1711666800 \
  --value-grouping-window=hour
{
  "object": "list",
  "data": [
    {
      "id": "mtrusg_test_6041CMAXJrFdZ56U76ce6L35Hz7xA3Tn58z5sY7bq6gM3XN5bx5Y459D4Xt2E17ko6M86kt7kV3bl5PM7LV59l4sY50b6oU5QD7bY3HP58z5sY7bq6gM3Y57LF2Dr7od3Hb8927gh4Tt4Lo4xO4ge60T81C6Y53gl4QS2D33ft3HC3Xl3bk3Cy3Cy",
      "object": "billing.meter_event_summary",
      "aggregated_value": 15,
      "end_time": 1711663200,
      "livemode": false,
      "meter": "mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA",
      "start_time": 1711659600
    },
    {
      "id": "mtrusg_test_6041CMAXJrFdZ56U76ce6L35Hz7xA3Tn58z5sY7bq6gM3XN5bx5Y459D4Xt2E17ko6M86kt7kV3bl5PM7LV59l4sY50b6oU5QD7bY3HP58z5sY7bq6gM3Y57LF2Dr7od3Hb8927gh4Tt4Lo4xO4ge60T81C6Y53gl4QS2D33ft3HC3Xi3Cy3Cy3Cy",
      "object": "billing.meter_event_summary",
      "aggregated_value": 10,
      "end_time": 1711659600,
      "livemode": false,
      "meter": "mtr_test_61Q8nQMqIFK9fRQmr41CMAXJrFdZ5MnA",
      "start_time": 1711656000
    }
  ],
  "has_more": false,
  "url": "/v1/billing/meters/:id/event_summa
{
  "id": "sub_1MowQVLkdIwHu7ixeRlqHVzs",
  "object": "subscription",
  "application": null,
  "application_fee_percent": null,
  "automatic_tax": {
    "enabled": false,
    "liability": null
  },
  "billing_cycle_anchor": 1679609767,
  "billing_thresholds": null,
  "cancel_at": null,
  "cancel_at_period_end": false,
  "canceled_at": null,
  "cancellation_details": {
    "comment": null,
    "feedback": null,
    "reason": null
  },
  "collection_method": "charge_automatically",
  "created": 1679609767,
  "currency": "usd",
  "current_period_end": 1682288167,
  "current_period_start": 1679609767,
  "customer": "cus_Na6dX7aXxi11N4",
  "days_until_due": null,
  "default_payment_method": null,
  "default_source": null,
  "default_tax_rates": [],
  "description": null,
  "discount": null,
  "discounts": null,
  "ended_at": null,
  "invoice_settings": {
    "issuer": {
      "type": "self"
    }
  },
  "items": {
    "object": "list",
    "data": [
      {
        "id": "ling_scheme": "per_unit",
          "created": 1679609766,
          "currency": "usd",
          "discounts": null,
          "interval": "month",
          "interval_count": 1,
          "livemode": false,
          "metadata": {},
          "nickname": null,
          "product": "prod_Na6dGcTsmU0I4R",
          "tiers_mode": null,
          "transform_usage": null,
          "trial_period_days": null,
          "usage_type": "licensed"
        },
        "price": {
          "id": "price_1MowQULkdIwHu7ixraBm864M",
          "object": "price",
          "active": true,
          "billing_scheme": "per_unit",
          "created": 1679609766,
          "currency": "usd",
          "custom_unit_amount": null,
          "livemode": false,
          "lookup_key": null,
          "metadata": {},
          "nickname": null,
          "product": "prod_Na6dGcTsmU0I4R",
          "recurring": {
            "aggregate_usage": null,
            "interval": "month",
            "interval_c
stripe subscriptions create  \
  --customer=cus_Na6dX7aXxi11N4 \
  -d "items[0][price]"=price_1MowQULkdIwHu7ixraBm864M
{
  "id": "sub_1MowQVLkdIwHu7ixeRlqHVzs",
  "object": "subscription",
  "application": null,
  "application_fee_percent": null,
  "automatic_tax": {
    "enabled": false,
    "liability": null
  },
  "billing_cycle_anchor": 1679609767,
  "billing_thresholds": null,
  "cancel_at": null,
  "cancel_at_period_end": false,
  "canceled_at": null,
  "cancellation_details": {
    "comment": null,
    "feedback": null,
    "reason": null
  },
  "collection_method": "charge_automatically",
  "created": 1679609767,
  "currency": "usd",
  "current_period_end": 1682288167,
  "current_period_start": 1679609767,
  "customer": "cus_Na6dX7aXxi11N4",
  "days_until_due": null,
  "default_payment_method": null,
  "default_source": null,
  "default_tax_rates": [],
  "description": null,
  "discount": null,
  "discounts": null,
  "ended_at": null,
  "invoice_settings": {
    "issuer": {
      "type": "self"
    }
  },
  "items": {
    "object": "list",
    "data": [
      {
        "id": "ubscription_item",
        "billing_thresholds": null,
        "created": 1679609768,
        "metadata": {},
        "plan": {
          "id": "price_1MowQULkdIwHu7ixraBm864M",
          "object": "plan",
          "active": true,
          "aggregate_usage": null,
          "amount": 1000,
          "amount_decimal": "1000",
          "billing_scheme": "per_unit",
          "created": 1679609766,
          "currency": "usd",
          "discounts": null,
          "interval": "month",
          "interval_count": 1,
          "livemode": false,
          "metadata": {},
          "nickname": null,
          "product": "prod_Na6dGcTsmU0I4R",
          "tiers_mode": null,
          "transform_usage": null,
          "trial_period_days": null,
          "usage_type": "licensed"
        },
        "price": {
          "id": "price_1MowQULkdIwHu7ixraBm864M",
          "object": "price",
          "active": true,
          "billing_scheme": "per_unit",
          "created": 1679609766,
stripe subscriptions update sub_1MowQVLkdIwHu7ixeRlqHVzs \
  -d "metadata[order_id]"=6735
{
  "id": "sub_1MowQVLkdIwHu7ixeRlqHVzs",
  "object": "subscription",
  "application": null,
  "application_fee_percent": null,
  "automatic_tax": {
    "enabled": false,
    "liability": null
  },
  "billing_cycle_anchor": 1679609767,
  "billing_thresholds": null,
  "cancel_at": null,
  "cancel_at_period_end": false,
  "canceled_at": null,
  "cancellation_details": {
    "comment": null,
    "feedback": null,
    "reason": null
  },
  "collection_method": "charge_automatically",
  "created": 1679609767,
  "currency": "usd",
  "current_period_end": 1682288167,
  "current_period_start": 1679609767,
  "customer": "cus_Na6dX7aXxi11N4",
  "days_until_due": null,
  "default_payment_method": null,
  "default_source": null,
  "default_tax_rates": [],
  "description": null,
  "discount": null,
  "discounts": null,
  "ended_at": null,
  "invoice_settings": {
    "issuer": {
      "type": "self"
    }
  },
  "items": {
    "object": "list",
    "data": [
      {
        "id": "unit_amount": null,
          "livemode": false,
          "lookup_key": null,
          "metadata": {},
          "nickname": null,
          "product": "prod_Na6dGcTsmU0I4R",
          "recurring": {
            "aggregate_usage": null,
            "interval": "month",
            "interval_count": 1,
            "trial_period_days": null,
            "usage_type": "licensed"
          },
          "tax_behavior": "unspecified",
          "tiers_mode": null,
          "transform_quantity": null,
          "type": "recurring",
          "unit_amount": 1000,
          "unit_amount_decimal": "1000"
        },
        "quantity": 1,
        "subscription": "sub_1MowQVLkdIwHu7ixeRlqHVzs",
        "tax_rates": []
      }
    ],
    "has_more": false,
    "total_count": 1,
    "url": "/v1/subscription_items?subscription=sub_1MowQVLkdIwHu7ixeRlqHVzs"
  },
  "latest_invoice": "in_1MowQWLkdIwHu7ixuzkSPfKd",
  "livemode": false,
  "metadata": {
    "order_id": "6735"
  },
  "next_pend
{
  "id": "sub_1MowQVLkdIwHu7ixeRlqHVzs",
  "object": "subscription",
  "application": null,
  "application_fee_percent": null,
  "automatic_tax": {
    "enabled": false,
    "liability": null
  },
  "billing_cycle_anchor": 1679609767,
  "billing_thresholds": null,
  "cancel_at": null,
  "cancel_at_period_end": false,
  "canceled_at": null,
  "cancellation_details": {
    "comment": null,
    "feedback": null,
    "reason": null
  },
  "collection_method": "charge_automatically",
  "created": 1679609767,
  "currency": "usd",
  "current_period_end": 1682288167,
  "current_period_start": 1679609767,
  "customer": "cus_Na6dX7aXxi11N4",
  "days_until_due": null,
  "default_payment_method": null,
  "default_source": null,
  "default_tax_rates": [],
  "description": null,
  "discount": null,
  "discounts": null,
  "ended_at": null,
  "invoice_settings": {
    "issuer": {
      "type": "self"
    }
  },
  "items": {
    "object": "list",
    "data": [
      {
        "id": "sage": null,
          "trial_period_days": null,
          "usage_type": "licensed"
        },
        "price": {
          "id": "price_1MowQULkdIwHu7ixraBm864M",
          "object": "price",
          "active": true,
          "billing_scheme": "per_unit",
          "created": 1679609766,
          "currency": "usd",
          "custom_unit_amount": null,
          "livemode": false,
          "lookup_key": null,
          "metadata": {},
          "nickname": null,
          "product": "prod_Na6dGcTsmU0I4R",
          "recurring": {
            "aggregate_usage": null,
            "interval": "month",
            "interval_count": 1,
            "trial_period_days": null,
            "usage_type": "licensed"
          },
          "tax_behavior": "unspecified",
          "tiers_mode": null,
          "transform_quantity": null,
          "type": "recurring",
          "unit_amount": 1000,
          "unit_amount_decimal": "1000"
        },
        "quantity": 1,
        "sub"
stripe subscriptions retrieve sub_1MowQVLkdIwHu7ixeRlqHVzs
{
  "id": "sub_1MowQVLkdIwHu7ixeRlqHVzs",
  "object": "subscription",
  "application": null,
  "application_fee_percent": null,
  "automatic_tax": {
    "enabled": false,
    "liability": null
  },
  "billing_cycle_anchor": 1679609767,
  "billing_thresholds": null,
  "cancel_at": null,
  "cancel_at_period_end": false,
  "canceled_at": null,
  "cancellation_details": {
    "comment": null,
    "feedback": null,
    "reason": null
  },
  "collection_method": "charge_automatically",
  "created": 1679609767,
  "currency": "usd",
  "current_period_end": 1682288167,
  "current_period_start": 1679609767,
  "customer": "cus_Na6dX7aXxi11N4",
  "days_until_due": null,
  "default_payment_method": null,
  "default_source": null,
  "default_tax_rates": [],
  "description": null,
  "discount": null,
  "discounts": null,
  "ended_at": null,
  "invoice_settings": {
    "issuer": {
      "type": "self"
    }
  },
  "items": {
    "object": "list",
    "data": [
      {
        "id": "          "product": "prod_Na6dGcTsmU0I4R",
          "tiers_mode": null,
          "transform_usage": null,
          "trial_period_days": null,
          "usage_type": "licensed"
        },
        "price": {
          "id": "price_1MowQULkdIwHu7ixraBm864M",
          "object": "price",
          "active": true,
          "billing_scheme": "per_unit",
          "created": 1679609766,
          "currency": "usd",
          "custom_unit_amount": null,
          "livemode": false,
          "lookup_key": null,
          "metadata": {},
          "nickname": null,
          "product": "prod_Na6dGcTsmU0I4R",
          "recurring": {
            "aggregate_usage": null,
            "interval": "month",
            "interval_count": 1,
            "trial_period_days": null,
            "usage_type": "licensed"
          },
          "tax_behavior": "unspecified",
          "tiers_mode": null,
          "transform_quantity": null,
          "type": "recurring",
          "unit_amount":
{
  "id": "sub_1MowQVLkdIwHu7ixeRlqHVzs",
  "object": "subscription",
  "application": null,
  "application_fee_percent": null,
  "automatic_tax": {
    "enabled": false,
    "liability": null
  },
  "billing_cycle_anchor": 1679609767,
  "billing_thresholds": null,
  "cancel_at": null,
  "cancel_at_period_end": false,
  "canceled_at": null,
  "cancellation_details": {
    "comment": null,
    "feedback": null,
    "reason": null
  },
  "collection_method": "charge_automatically",
  "created": 1679609767,
  "currency": "usd",
  "current_period_end": 1682288167,
  "current_period_start": 1679609767,
  "customer": "cus_Na6dX7aXxi11N4",
  "days_until_due": null,
  "default_payment_method": null,
  "default_source": null,
  "default_tax_rates": [],
  "description": null,
  "discount": null,
  "discounts": null,
  "ended_at": null,
  "invoice_settings": {
    "issuer": {
      "type": "self"
    }
  },
  "items": {
    "object": "list",
    "data": [
      {
        "id": "          "interval_count": 1,
            "trial_period_days": null,
            "usage_type": "licensed"
          },
          "tax_behavior": "unspecified",
          "tiers_mode": null,
          "transform_quantity": null,
          "type": "recurring",
          "unit_amount": 1000,
          "unit_amount_decimal": "1000"
        },
        "quantity": 1,
        "subscription": "sub_1MowQVLkdIwHu7ixeRlqHVzs",
        "tax_rates": []
      }
    ],
    "has_more": false,
    "total_count": 1,
    "url": "/v1/subscription_items?subscription=sub_1MowQVLkdIwHu7ixeRlqHVzs"
  },
  "latest_invoice": "in_1MowQWLkdIwHu7ixuzkSPfKd",
  "livemode": false,
  "metadata": {},
  "next_pending_invoice_item_invoice": null,
  "on_behalf_of": null,
  "pause_collection": null,
  "payment_settings": {
    "payment_method_options": null,
    "payment_method_types": null,
    "save_default_payment_method": "off"
  },
  "pending_invoice_item_interval": null,
  "pending_setup_intent": null,
  "


  "business_type": null,
"capabilities": {},
"charges_enabled": false,
"controller": {
    "fees": {
        "payer": "application"
    },
    "is_controller": true,
    "losses": {
        "payments": "application"
    },
    "requirement_collection": "stripe",
    "stripe_dashboard": {
        "type": "express"
    },
    "type": "application"
},
"country": "US",
"created": 1695830751,
"default_currency": "usd",
"details_submitted": false,
"email": "jenny.rosen@example.com",
"external_accounts": {
    "object": "list",
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/accounts/acct_1Nv0FGQs_acceptance.date",
    "tos_acceptance.ip"
],
"pending_verification": []
},
"settings": {
    "bacs_debit_payments": {
        "display_name": null,
        "service_user_number": null
    },
    "branding": {
        "icon": null,
        "logo": null,
        "primary_color": null,
        "secondary_color": null
    },
    "card_issuing": {
        "tos_acceptance": {
            "date": null,
            "ip": null
        }
    },
    "card_payments": {
        "decline_on": {
            "avs_failure": false,
            "cvc_failure": false
        },
        "statement_descriptor_prefix": null,
        "statement_descriptor_prefix_kanji": null,
        "statement_descriptor_prefix_kana": null
    },
    "dashboard": {
        "display_name": null,
        "timezone": "Etc/UTC"
    },
    "invoices": {
        "default_account_tax_ids": null
    },
    "payments": {
        "statement_descriptor": null,
        "statement_descriptor_kana": null,
        "statement_descriptor_kanji": null
    },

    stripe accounts list \
                    - -limit = 3
{
    "object": "list",
    "url": "/v1/accounts",
    "has_more": false,
    "data": [
        {
            "id": "acct_1Nv0FGQ9RKHgCVdK",
            "object": "account",
            "business_profile": {
                "annual_revenue": null,
                "estimated_worker_count": null,
                "mcc": null,
                "name": null,
                "product_description": null,
                "support_address": null,
                "support_email": null,
                "support_phone": null,
                "support_url": null,
                "url": null
            },
            "business_type": null,
            "capabilities": {},
            "charges_enabled": false,
            "controller": {
                "fees": {
                    "payer": "application"
                },
                "is_controller": true,
                "losses": {
                    "payments": "application"
                },
                "requirement_collection": "stripe",
                "stripe_dashboard": {
                    "type": "express"
                },
                "type": "application"
            },
            "country": "US",
            "created": 1695830751,
            "default_currency": "us{
                                "alternatives": [],
"current_deadline": null,
"currently_due": [
    "business_profile.mcc",
    "business_profile.url",
    "business_type",
    "external_account",
    "representative.first_name",
    "representative.last_name",
    "tos_acceptance.date",
    "tos_acceptance.ip"
],
"disabled_reason": "requirements.past_due",
"errors": [],
"eventually_due": [
    "business_profile.mcc",
    "business_profile.url",
    "business_type",
    "external_account",
    "representative.first_name",
    "representative.last_name",
    "tos_acceptance.date",
    "tos_acceptance.ip"
],
"past_due": [
    "business_profile.mcc",
    "business_profile.url",
    "business_type",
    "external_account",
    "representative.first_name",
    "representative.last_name",
    "tos_acceptan
    stripe accounts delete acct_1032D82eZvKYlo2C
    {
        "id": "acct_1Nv0FGQ9RKHgCVdK",
        "object": "account",
        "deleted": true
    }
    stripe accounts reject acct_1032D82eZvKYlo2C \
                           - -reason = fraud
{
    "id": "acct_1Nv0FGQ9RKHgCVdK",
    "object": "account",
    "business_profile": {
        "annual_revenue": null,
        "estimated_worker_count": null,
        "mcc": null,
        "name": null,
        "product_description": null,
        "support_address": null,
        "support_email": null,
        "support_phone": null,
        "support_url": null,
        "url": null
    },
    "business_type": null,
    "capabilities": {},
    "charges_enabled": false,
    "controller": {
        "fees": {
            "payer": "application"
        },
        "is_controller": true,
        "losses": {
            "payments": "application"
        },
        "requirement_collection": "stripe",
        "stripe_dashboard": {
            "type": "express"
        },
        "type": "application"
    },
    "country": "US",
    "created": 1385798567,
    "default_currency": "usd",
    "details_submitted": true,
    "email": "jenny.rosen@example.com",
    "external_accounts": {
        "object": "list",
        "data": [],
        "has_more": false,
        "total_count": 0,
        "url": "/v1/accounts/acct_1Nv0FGQ9 [],
               "current_deadline": null,
"currently_due": [
    "business_profile.mcc",
    "business_profile.product_description",
    "business_profile.support_phone",
    "business_profile.url",
    "business_type",
    "external_account",
    "person_8UayFKIMRJklog.first_name",
    "person_8UayFKIMRJklog.last_name",
    "tos_acceptance.date",
    "tos_acceptance.ip"
],
"disabled_reason": "rejected.fraud",
"errors": [],
"eventually_due": [
    "business_profile.mcc",
    "business_profile.product_description",
    "business_profile.support_phone",
    "business_profile.url",
    "business_type",
    "external_account",
    "person_8UayFKIMRJklog.first_name",
    "person_8UayFKIMRJklog.last_name",
    "tos_acceptance.date",
    "tos_acceptance.ip"
],
"past_due": [
    "business_profile.mcc",
    "business_profile.product_description",
    "business_profile.support_phone",
    "business_profile.url",

    {
        "object": "login_link",
        "created": 1686084879,
        "url": "https://connect.stripe.com/express/acct_1032D82eZvKYlo2C/F44eiGHh5sEV"
    }
    stripe login_links create acct_1032D82eZvKYlo2C
    {
        "object": "login_link",
        "created": 1686084879,
        "url": "https://connect.stripe.com/express/acct_1032D82eZvKYlo2C/F44eiGHh5sEV"
    }

    stripe account_links create \
                         - -account = acct_1Mt0CORHFI4mz9Rw \
                                      - -refresh - url = "https://example.com/reauth" \
                                                         - -
return -url="https://example.com/return" \
            - -type = account_onboarding
{
    "object": "account_link",
    "created": 1680577733,
    "expires_at": 1680578033,
    "url": "https://connect.stripe.com/setup/c/acct_1Mt0CORHFI4mz9Rw/TqckGNUHg2mG"
}
stripe
account_links
create \
- -account = acct_1Mt0CORHFI4mz9Rw \
    stripe
account_links
create \
- -account = acct_1Mt0CORHFI4mz9Rw \
    stripe
account_links
create \
- -account = acct_1Mt0CORHFI4mz9Rw \
             - -refresh - url = "https://webtechnicom.net/reauth"
--
return -url="https://webtechnicom.net/return"
--type = account_onboarding
{
    "object": "account_link",
    "created": 1680577733,
    "expires_at": 1680578033,
    "url": "https://connect.stripe.com/setup/c/acct_1Mt0CORHFI4mz9Rw/TqckGNUHg2mG"
}
stripe
account_sessions
create \
- -account = acct_1NkDjjJyhOZfPCWt \
             - d
"components[account_onboarding][enabled]" = true \
                                            - d
"components[payments][enabled]" = true \
                                  - d
"components[payouts][enabled]" = true \
                                 - d
"components[balances][enabled]" = true
{
    "object": "account_session",
    "account": "acct_1NkDjjJyhOZfPCWt",
    "client_secret": "_OXIKXxEihJokDBnDoe2sgG5OGSO2Q12shKvbeboxpALZGng",
    "expires_at": 1693261123,
    "livemode": false,
    "components": {
        "account_management": {
            "enabled": false,
            "features": {
                "external_account_collection": true
            }
        },
        "account_onboarding": {
            "enabled": true,
            "features": {
                "external_account_collection": true
            }
        },
        "balances": {
            "enabled": true,
            "features": {
                "edit_payout_schedule": false,
                "instant_payouts": false,
                "standard_payouts": false,
                "external_account_collection": true
            }
        },
        "documents": {
            "enabled": false,
            "features": {}
        },
        "notification_banner": {
            "enabled": false,
            "features": {
                "external_account_collection": true
            }
        },
        "payment_details": {
            "enabled": false,
            "features": {
                "captings": {
                    "enabled": false,
                    "features": {}
                }
            }
        }
        {
            "id": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
            "object": "application_fee",
            "account": "acct_164wxjKbnvuxQXGu",
            "amount": 105,
            "amount_refunded": 105,
            "application": "ca_32D88BD1qLklliziD7gYQvctJIhWBSQ7",
            "balance_transaction": "txn_1032HU2eZvKYlo2CEPtcnUvl",
            "charge": "ch_1B73DOKbnvuxQXGurbwPqzsu",
            "created": 1506609734,
            "currency": "gbp",
            "livemode": false,
            "originating_transaction": null,
            "refunded": true,
            "refunds": {
                "object": "list",
                "data": [
                    {
                        "id": "fr_1MBoV6KbnvuxQXGucP0PaPPO",
                        "object": "fee_refund",
                        "amount": 0,
                        "balance_transaction": null,
                        "created": 1670284508,
                        "currency": "usd",
                        "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
                        "metadata": {}
                    },
                    {
                        "id": "fr_1MBoU0KbnvuxQXGu2wCCz4Bb",
                        "object": "fee_refund",
                        "amount": 0,
                        "balance_transaction": null,
                        "created": 1670284441,
                        "currency": "usd",
                        "fee": "fee_1B73DO       "id": "fr_1MBoPOKbnvuxQXGueOBnke22",
                                                                                   "object": "fee_refund",
        "amount": 0,
        "balance_transaction": null,
        "created": 1670284154,
        "currency": "usd",
        "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
        "metadata": {}
    },
    {
        "id": "fr_1MBoOGKbnvuxQXGu6EPQI2Zp",
        "object": "fee_refund",
        "amount": 0,
        "balance_transaction": null,
        "created": 1670284084,
        "currency": "usd",
        "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
        "metadata": {}
    },
{
    "id": "fr_1MBoMUKbnvuxQXGu8Y0Peaoy",
    "object": "fee_refund",
    "amount": 0,
    "balance_transaction": null,
    "created": 1670283974,
    "currency": "usd",
    "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
    "metadata": {}
},
{
    "id": "fr_1MAgZBKbnvuxQXGuLTUrgGeq",
    "object": "fee_refund",
    "amount": 0,
    "balance_transaction": null,
    "created
        stripe application_fees retrieve fee_1B73DOKbnvuxQXGuhY8Aw0TN
    {
        "id": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
        "object": "application_fee",
        "account": "acct_164wxjKbnvuxQXGu",
        "amount": 105,
        "amount_refunded": 105,
        "application": "ca_32D88BD1qLklliziD7gYQvctJIhWBSQ7",
        "balance_transaction": "txn_1032HU2eZvKYlo2CEPtcnUvl",
        "charge": "ch_1B73DOKbnvuxQXGurbwPqzsu",
        "created": 1506609734,
        "currency": "gbp",
        "livemode": false,
        "originating_transaction": null,
        "refunded": true,
        "refunds": {
            "object": "list",
            "data": [
                {
                    "id": "fr_1MBoV6KbnvuxQXGucP0PaPPO",
                    "object": "fee_refund",
                    "amount": 0,
                    "balance_transaction": null,
                    "created": 1670284508,
                    "currency": "usd",
                    "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
                    "metadata": {}
                },
                {
                    "id": "fr_1MBoU0KbnvuxQXGu2wCCz4Bb",
                    "object": "fee_refund",
                    "amount": 0,
                    "balance_transaction": null,
                    "created": 1670284441,
                    "currency": "usd",
                    "fee": "fee_1B73DO "created": 1670284084,
                                               "currency": "usd",
"fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
"metadata": {}
},
{
    "id": "fr_1MBoMUKbnvuxQXGu8Y0Peaoy",
    "object": "fee_refund",
    "amount": 0,
    "balance_transaction": null,
    "created": 1670283974,
    "currency": "usd",
    "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
    "metadata": {}
},
{
    "id": "fr_1MAgZBKbnvuxQXGuLTUrgGeq",
    "object": "fee_refund",
    "amount": 0,
    "balance_transaction": null,
    "created": 1670015681,
    "currency": "usd",
    "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
    "metadata": {}
},
{
    "id": "fr_1JAu9EKbnvuxQXGuRdZYkxVW",
    "object": "fee_refund",
    "amount": 0,
    "balance_transaction": null,
    "created": 1625738880,
    "currency": "usd",
    "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
    "metadata": {
        "order_id": "6735"

        stripe application_fees list \
                                - -limit = 3
{
    "object": "list",
    "url": "/v1/application_fees",
    "has_more": false,
    "data": [
        {
            "id": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
            "object": "application_fee",
            "account": "acct_164wxjKbnvuxQXGu",
            "amount": 105,
            "amount_refunded": 105,
            "application": "ca_32D88BD1qLklliziD7gYQvctJIhWBSQ7",
            "balance_transaction": "txn_1032HU2eZvKYlo2CEPtcnUvl",
            "charge": "ch_1B73DOKbnvuxQXGurbwPqzsu",
            "created": 1506609734,
            "currency": "gbp",
            "livemode": false,
            "originating_transaction": null,
            "refunded": true,
            "refunds": {
                "object": "list",
                "data": [
                    {
                        "id": "fr_1MBoV6KbnvuxQXGucP0PaPPO",
                        "object": "fee_refund",
                        "amount": 0,
                        "balance_transaction": null,
                        "created": 1670284508,
                        "currency": "usd",
                        "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
                        "metadata": {}
                    },
                    {
                        "id": "f          "object": "fee_refund",
                                                               "amount": 0,
"balance_transaction": null,
"created": 1670284441,
"currency": "usd",
"fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
"metadata": {}
},
{
    "id": "fr_1MBoRzKbnvuxQXGuvKkBKkSR",
    "object": "fee_refund",
    "amount": 0,
    "balance_transaction": null,
    "created": 1670284315,
    "currency": "usd",
    "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
    "metadata": {}
},
{
    "id": "fr_1MBoPOKbnvuxQXGueOBnke22",
    "object": "fee_refund",
    "amount": 0,
    "balance_transaction": null,
    "created": 1670284154,
    "currency": "usd",
    "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
    "metadata": {}
},
{
    "id": "fr_1MBoOGKbnvuxQXGu6EPQI2Zp",
    {"object": "fee_refund",
     "id": "fr_1MtJRpKbnvuxQXGuM6Ww0D24",
     "object": "fee_refund",
     "amount": 100,
     "balance_transaction": null,
     "created": 1680651573,
     "currency": "usd",
     "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
     "metadata": {}
     }
        stripe fee_refunds create fee_1B73DOKbnvuxQXGuhY8Aw0TN
    {
        "id": "fr_1MtJRpKbnvuxQXGuM6Ww0D24",
        "object": "fee_refund",
        "amount": 100,
        "balance_transaction": null,
        "created": 1680651573,
        "currency": "usd",
        "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
        "metadata": {}
    }
    stripe fee_refunds update fee_1B73DOKbnvuxQXGuhY8Aw0TN fr_1MtJRpKbnvuxQXGuM6Ww0D24 \
                                                           - d "metadata[order_id]" = 6735
{
    "id": "fr_1MtJRpKbnvuxQXGuM6Ww0D24",
    "object": "fee_refund",
    "amount": 100,
    "balance_transaction": null,
    "created": 1680651573,
    "currency": "usd",
    "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
    "metadata": {
        "order_id": "6735"
    }
}
stripe
fee_refunds
retrieve
fee_1B73DOKbnvuxQXGuhY8Aw0TN
fr_1MtJRpKbnvuxQXGuM6Ww0D24
{
    "id": "fr_1MtJRpKbnvuxQXGuM6Ww0D24",
    "object": "fee_refund",
    "amount": 100,
    "balance_transaction": null,
    "created": 1680651573,
    "currency": "usd",
    "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
    "metadata": {}
}
stripe
fee_refunds
list
fr_1MtJRpKbnvuxQXGuM6Ww0D24 \
- -limit = 3
{
    "object": "list",
    "url": "/v1/application_fees/fr_1MtJRpKbnvuxQXGuM6Ww0D24/refunds",
    "has_more": false,
    "data": [
        {
            "id": "fr_1MtJRpKbnvuxQXGuM6Ww0D24",
            "object": "fee_refund",
            "amount": 100,
            "balance_transaction": null,
            "created": 1680651573,
            "currency": "usd",
            "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
            "metadata": {}
        }
        {...}
        {...}
    ],
}
{
    "id": "card_payments",
    "object": "capability",
    "account": "acct_1032D82eZvKYlo2C",
    "future_requirements": {
        "alternatives": [],
        "current_deadline": null,
        "currently_due": [],
        "disabled_reason": null,
        "errors": [],
        "eventually_due": [],
        "past_due": [],
        "pending_verification": []
    },
    "requested": true,
    "requested_at": 1688491010,
    "requirements": {
        "alternatives": [],
        "current_deadline": null,
        "currently_due": [],
        "disabled_reason": null,
        "errors": [],
        "eventually_due": [],
        "past_due": [],
        "pending_verification": []
    },
    "status": "inactive"
}
stripe
capabilities
update
acct_1032D82eZvKYlo2C
card_payments \
- -requested = true
{
    "id": "card_payments",
    "object": "capability",
    "account": "acct_1032D82eZvKYlo2C",
    "future_requirements": {
        "alternatives": [],
        "current_deadline": null,
        "currently_due": [],
        "disabled_reason": null,
        "errors": [],
        "eventually_due": [],
        "past_due": [],
        "pending_verification": []
    },
    "requested": true,
    "requested_at": 1688491010,
    "requirements": {
        "alternatives": [],
        "current_deadline": null,
        "currently_due": [],
        "disabled_reason": null,
        "errors": [],
        "eventually_due": [],
        "past_due": [],
        "pending_verification": []
    },
    "status": "inactive"
}
stripe
capabilities
retrieve
acct_1032D82eZvKYlo2C
card_payments
{
    "id": "card_payments",
    "object": "capability",
    "account": "acct_1032D82eZvKYlo2C",
    "future_requirements": {
        "alternatives": [],
        "current_deadline": null,
        "currently_due": [],
        "disabled_reason": null,
        "errors": [],
        "eventually_due": [],
        "past_due": [],
        "pending_verification": []
    },
    "requested": true,
    "requested_at": 1688491010,
    "requirements": {
        "alternatives": [],
        "current_deadline": null,
        "currently_due": [],
        "disabled_reason": null,
        "errors": [],
        "eventually_due": [],
        "past_due": [],
        "pending_verification": []
    },
    "status": "inactive"
}
stripe
accounts
capabilities
acct_1032D82eZvKYlo2C
{
    "object": "list",
    "url": "/v1/accounts/acct_1032D82eZvKYlo2C/capabilities",
    "has_more": false,
    "data": [
        {
            "id": "card_payments",
            "object": "capability",
            "account": "acct_1032D82eZvKYlo2C",
            "future_requirements": {
                "alternatives": [],
                "current_deadline": null,
                "currently_due": [],
                "disabled_reason": null,
                "errors": [],
                "eventually_due": [],
                "past_due": [],
                "pending_verification": []
            },
            "requested": true,
            "requested_at": 1693951912,
            "requirements": {
                "alternatives": [],
                "current_deadline": null,
                "currently_due": [],
                "disabled_reason": null,
                "errors": [],
                "eventually_due": [],
                "past_due": [],
                "pending_verification": []
            },
            "status": "inactive"
        }
    ]
}
{
    "id": "ba_1N9DrD2eZvKYlo2C58f4DaIa",
    "object": "bank_account",
    "account": "acct_1032D82eZvKYlo2C",
    "account_holder_name": "Jane Austen",
    "account_holder_type": "individual",
    "account_type": null,
    "available_payout_methods": [
        "standard"
    ],
    "bank_name": "STRIPE TEST BANK",
    "country": "US",
    "currency": "usd",
    "fingerprint": "1JWtPxqbdX5Gamtz",
    "last4": "6789",
    "metadata": {},
    "routing_number": "110000000",
    "status": "new"
}
stripe
external_accounts
create
acct_1032D82eZvKYlo2C \
- -external - account = btok_1NAiJy2eZvKYlo2Cnh6bIs9c
{
    "id": "ba_1NAiJy2eZvKYlo2CvChQKz5k",
    "object": "bank_account",
    "account": "acct_1032D82eZvKYlo2C",
    "account_holder_name": "Jane Austen",
    "account_holder_type": "company",
    "account_type": null,
    "bank_name": "STRIPE TEST BANK",
    "country": "US",
    "currency": "usd",
    "fingerprint": "1JWtPxqbdX5Gamtc",
    "last4": "6789",
    "metadata": {},
    "routing_number": "110000000",
    "status": "
    stripe external_accounts update acct_1032D82eZvKYlo2C ba_1NAiwl2eZvKYlo2CRdCLZSxO \
                                                          - d "metadata[order_id]" = 6735
{
    "id": "ba_1NAiwl2eZvKYlo2CRdCLZSxO",
    "object": "bank_account",
    "account_holder_name": "Jane Austen",
    "account_holder_type": "company",
    "account_type": null,
    "bank_name": "STRIPE TEST BANK",
    "country": "US",
    "currency": "usd",
    "fingerprint": "1JWtPxqbdX5Gamtc",
    "last4": "6789",
    "metadata": {
        "order_id": "6735"
    },
    "routing_number": "110000000",
    "status": "new",
    "account": "acct_1032D82eZvKYlo2C"
}
stripe
external_accounts
retrieve
acct_1032D82eZvKYlo2C
ba_1NAinX2eZvKYlo2CpFGcuuEG
{
    "id": "ba_1NAinX2eZvKYlo2CpFGcuuEG",
    "object": "bank_account",
    "account_holder_name": "Jane Austen",
    "account_holder_type": "company",
    "account_type": null,
    "bank_name": "STRIPE TEST BANK",
    "country": "US",
    "currency": "usd",
    "customer": null,
    "fingerprint": "1JWtPxqbdX5Gamtc",
    "last4": "6789",
    "metadata": {},
    "routing_number": "110000000",
    "status": "new"
}
stripe
external_accounts
list
acct_1032D82eZvKYlo2C \
- -object = bank_account
{
    "object": "list",
    "url": "/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts",
    "has_more": false,
    "data": [
        {
            "id": "ba_1NB1IV2eZvKYlo2CByiLrMWv",
            "object": "bank_account",
            "account_holder_name": "Jane Austen",
            "account_holder_type": "company",
            "account_type": null,
            "bank_name": "STRIPE TEST BANK",
            "country": "US",
            "currency": "usd",
            "fingerprint": "1JWtPxqbdX5Gamtc",
            "last4": "6789",
            "metadata": {},
            "routing_number": "110000000",
            "status": "new",
            "account": "acct_1032D82eZvKYlo2C"
        }
        {...}
        {...}
    ],
}

stripe
external_accounts
delete
acct_1032D82eZvKYlo2C
ba_1NAz2w2eZvKYlo2CgeR2w6yU
{
    "id": "ba_1NAz2w2eZvKYlo2CgeR2w6yU",
    "object": "bank_account",
    "deleted": true
}

{
    "id": "card_1MvoiELkdIwHu7ixOeFGbN9D",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "US",
    "customer": "cus_NhD8HD2bY8dP3V",
    "cvc_check": null,
    "dynamic_last4": null,
    "exp_month": 4,
    "exp_year": 2024,
    "fingerprint": "mToisGZ01V71BCos",
    "funding": "credit",
    "last4": "4242",
    "metadata": {},
    "name": null,
    "tokenization_method": null,
    "wallet": null
}
stripe
external_accounts
create
acct_1032D82eZvKYlo2C \
- -external - account = tok_visa_debit
{
    "id": "card_1NAiaG2eZvKYlo2CDXvcMb6m",
    "object": "card",
    "account": "acct_1032D82eZvKYlo2C",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "US",
    "cvc_check": "pass",
    "dynamic_last4": null,
    "exp_month": 8,
    "exp_year": 2024,
    "fingerprint": "Xt5EWLLDS7FJjR1c",
    "funding": "credit",
    "last4": "4242",
    "metadata": {},
    "name": null,
    "redaction": null,
    "tokenization_method": null,
    "wallet": null
}
stripe
external_accounts
update
acct_1032D82eZvKYlo2C
card_1NBLeN2eZvKYlo2CIq1o7Pzs \
- d
"metadata[order_id]" = 6735
{
    "id": "card_1NBLeN2eZvKYlo2CIq1o7Pzs",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "US",
    "cvc_check": "pass",
    "dynamic_last4": null,
    "exp_month": 8,
    "exp_year": 2024,
    "fingerprint": "Xt5EWLLDS7FJjR1c",
    "funding": "credit",
    "last4": "4242",
    "metadata": {
        "order_id": "6735"
    },
    "name": "Jenny Rosen",
    "redaction": null,
    "tokenization_method": null,
    "wallet": null,
    "account": "acct_1032D82eZvKYlo2C"
}
stripe
external_accounts
retrieve
acct_1032D82eZvKYlo2C
card_1NAinb2eZvKYlo2C1Fm9mZsu
{
    "id": "card_1NAinb2eZvKYlo2C1Fm9mZsu",
    "object": "card",
    "address_city": null,
    "address_country": null,
    "address_line1": null,
    "address_line1_check": null,
    "address_line2": null,
    "address_state": null,
    "address_zip": null,
    "address_zip_check": null,
    "brand": "Visa",
    "country": "US",
    "cvc_check": "pass",
    "dynamic_last4": null,
    "exp_month": 8,
    "exp_year": 2024,
    "fingerprint": "Xt5EWLLDS7FJjR1c",
    "funding": "credit",
    "last4": "4242",
    "metadata": {},
    "name": null,
    "redaction": null,
    "tokenization_method": null,
    "wallet": null,
    "account": "acct_1032D82eZvKYlo2C"
}
stripe
external_accounts
list
acct_1032D82eZvKYlo2C \
- -object = card
{
    "object": "list",
    "url": "/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts",
    "has_more": false,
    "data": [
        {
            "id": "card_1NAz2x2eZvKYlo2C75wJ1YUs",
            "object": "card",
            "address_city": null,
            "address_country": null,
            "address_line1": null,
            "address_line1_check": null,
            "address_line2": null,
            "address_state": null,
            "address_zip": null,
            "address_zip_check": null,
            "brand": "Visa",
            "country": "US",
            "cvc_check": "pass",
            "dynamic_last4": null,
            "exp_month": 8,
            "exp_year": 2024,
            "fingerprint": "Xt5EWLLDS7FJjR1c",
            "funding": "credit",
            "last4": "4242",
            "metadata": {},
            "name": null,
            "redaction": null,
            "tokenization_method": null,
            "wallet": null,
            "account": "acct_1032D82eZvKYlo2C"
        }
        {...}
        {...}
    ],
}
stripe
external_accounts
delete
acct_1032D82eZvKYlo2C
card_1NAz2x2eZvKYlo2C75wJ1YUs
{
    "id": "card_1NAz2x2eZvKYlo2C75wJ1YUs",
    "object": "card",
    "deleted": true
}
stripe
persons
create
acct_1032D82eZvKYlo2C
{
    "id": "person_1N9XNb2eZvKYlo2CjPX7xF6F",
    "object": "person",
    "account": "acct_1032D82eZvKYlo2C",
    "created": 1684518375,
    "dob": {
        "day": null,
        "month": null,
        "year": null
    },
    "first_name": null,
    "future_requirements": {
        "alternatives": [],
        "currently_due": [],
        "errors": [],
        "eventually_due": [],
        "past_due": [],
        "pending_verification": []
    },
    "id_number_provided": false,
    "last_name": null,
    "metadata": {},
    "relationship": {
        "director": false,
        "executive": false,
        "owner": false,
        "percent_ownership": null,
        "representative": false,
        "title": null
    },
    "requirements": {
        "alternatives": [],
        "currently_due": [],
        "errors": [],
        "eventually_due": [],
        "past_due": [],
        "pending_verification": []
    },
    "ssn_last_4_provided": false,
    "verification": {
        "additional_document": {
            "back": null,
            "details": null,
            "details_code": null,
            "front": null

            stripe persons update acct_1032D82eZvKYlo2C person_1MqjB62eZvKYlo2CaeEJzKVR \
                                                        - d "metadata[order_id]" = 6735
{
    "id": "person_1MqjB62eZvKYlo2CaeEJzKVR",
    "person": "person_1MqjB62eZvKYlo2CaeEJzKVR",
    "object": "person",
    "account": "acct_1032D82eZvKYlo2C",
    "created": 1680035496,
    "dob": {
        "day": null,
        "month": null,
        "year": null
    },
    "first_name": "Jane",
    "future_requirements": {
        "alternatives": [],
        "currently_due": [],
        "errors": [],
        "eventually_due": [],
        "past_due": [],
        "pending_verification": []
    },
    "id_number_provided": false,
    "last_name": "Diaz",
    "metadata": {
        "order_id": "6735"
    },
    "relationship": {
        "director": false,
        "executive": false,
        "owner": false,
        "percent_ownership": null,
        "representative": false,
        "title": null
    },
    "requirements": {
        "alternatives": [],
        "currently_due": [],
        "errors": [],
        "eventually_due": [],
        "past_due": [],
        "pending_verification": []
    },
    "ssn_last_4_provided": false,
    "verification": {
        "additional_document": {
            "back": nucode": null,
                          "front": null
        },
        "details": null,
        "details_code": null,
        "document": {
            "back": null,
            "details": null,
            "details_code": null,
            "front": null
        },
        "status": "unverified"
    }
}
stripe
persons
retrieve
acct_1032D82eZvKYlo2C
person_1MqjB62eZvKYlo2CaeEJzKVR
{
    "id": "person_1N9XNb2eZvKYlo2CjPX7xF6F",
    "object": "person",
    "account": "acct_1032D82eZvKYlo2C",
    "created": 1684518375,
    "dob": {
        "day": null,
        "month": null,
        "year": null
    },
    "first_name": null,
    "future_requirements": {
        "alternatives": [],
        "currently_due": [],
        "errors": [],
        "eventually_due": [],
        "past_due": [],
        "pending_verification": []
    },
    "id_number_provided": false,
    "last_name": null,
    "metadata": {},
    "relationship": {
        "director": false,
        "executive": false,
        "owner": false,
        "percent_ownership": null,
        "representative": false,
        "title": null
    },
    "requirements": {
        "alternatives": [],
        "currently_due": [],
        "errors": [],
        "eventually_due": [],
        "past_due": [],
        "pending_verification": []
    },
    "ssn_last_4_provided": false,
    "verification": {
        "additional_document": {
            "back": null,
            "details": null,
            "details_code": null,
            "front": null

            stripe accounts persons acct_1032D82eZvKYlo2C \
                                    - -limit = 3
{
    "object": "list",
    "url": "/v1/accounts/acct_1032D82eZvKYlo2C/persons",
    "has_more": false,
    "data": [
        {
            "id": "person_1MqjB62eZvKYlo2CaeEJzKVR",
            "person": "person_1MqjB62eZvKYlo2CaeEJzKVR",
            "object": "person",
            "account": "acct_1032D82eZvKYlo2C",
            "created": 1680035496,
            "dob": {
                "day": null,
                "month": null,
                "year": null
            },
            "first_name": "Jane",
            "future_requirements": {
                "alternatives": [],
                "currently_due": [],
                "errors": [],
                "eventually_due": [],
                "past_due": [],
                "pending_verification": []
            },
            "id_number_provided": false,
            "last_name": "Diaz",
            "metadata": {},
            "relationship": {
                "director": false,
                "executive": false,
                "owner": false,
                "percent_ownership": null,
                "representative": false,
                "title": null
            },
            "requirements": {
                "alternatives": [],
                "cur
                    stripe persons delete acct_1032D82eZvKYlo2C person_1MqjB62eZvKYlo2CaeEJzKVR
                stripe persons delete acct_1032D82eZvKYlo2C person_1MqjB62eZvKYlo2CaeEJzKVR
                    {
                        "id": "person_1MqjB62eZvKYlo2CaeEJzKVR",
                        "object": "person",
                        "deleted": true
                    }
                {
                    "id": "iauth_1JVXl82eZvKYlo2CPIiWlzrn",
                    "object": "issuing.authorization",
                    "amount": 382,
                    "amount_details": {
                        "atm_fee": null
                    },
                    "approved": false,
                    "authorization_method": "online",
                    "balance_transactions": [],
                    "card": {
                        "id": "ic_1JDmgz2eZvKYlo2CRXlTsXj6",
                        "object": "issuing.card",
                        "brand": "Visa",
                        "cancellation_reason": null,
                        "cardholder": {
                            "id": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",
                            "object": "issuing.cardholder",
                            "billing": {
                                "address": {
                                    "city": "San Francisco",
                                    "country": "US",
                                    "line1": "123 Main Street",
                                    "line2": null,
                                    "postal_code": "94111",
                                    "state": "CA"
                                }
                            },
                            "company": null,
                            "created": 1626425119,
                            "email": "jenny.rosen@example.com",
                            "individual": null,
                            "livemode": false,
                            "metadata": {},
                            "name": "Jenny Rosen",
                            "phone_number": "+18008675309",
                            "redaction": null,
                            "requirem   "replacement_reason": null,
                                                           "shipping": null,
                            "spending_controls": {
                                "allowed_categories": null,
                                "blocked_categories": null,
                                "spending_limits": [
                                    {
                                        "amount": 50000,
                                        "categories": [],
                                        "interval": "daily"
                                    }
                                ],
                                "spending_limits_currency": "usd"
                            },
                            "status": "active",
                            "type": "virtual",
                            "wallets": {
                                "apple_pay": {
                                    "eligible": true,
                                    "ineligible_reason": null
                                },
                                "google_pay": {
                                    "eligible": true,
                                    "ineligible_reason": null
                                },
                                "primary_account_identifier": null
                            }
                        },
                        "cardholder": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",
                        "created": 1630657706,
                        "currency": "usd",
                        "livemode": false,
                        "merchant_amount": 382,
                        "merchant_currency": "usd",
                        "merchant_data": {
                            "category": "computer_software_stores",
                            "category_code": "5734",
                            "city": "SAN FRANCISCO",
                            "country": "US",
                            "name": "STRIPE",
                            "network_i
                                stripe issuing authorizations update iauth_1JVXl82eZvKYlo2CPIiWlzrn \
                                                                     - d "metadata[order_id]" = 6735
{
    "id": "iauth_1JVXl82eZvKYlo2CPIiWlzrn",
    "object": "issuing.authorization",
    "amount": 382,
    "amount_details": {
        "atm_fee": null
    },
    "approved": false,
    "authorization_method": "online",
    "balance_transactions": [],
    "card": {
        "id": "ic_1JDmgz2eZvKYlo2CRXlTsXj6",
        "object": "issuing.card",
        "brand": "Visa",
        "cancellation_reason": null,
        "cardholder": {
            "id": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",
            "object": "issuing.cardholder",
            "billing": {
                "address": {
                    "city": "San Francisco",
                    "country": "US",
                    "line1": "123 Main Street",
                    "line2": null,
                    "postal_code": "94111",
                    "state": "CA"
                }
            },
            "company": null,
            "created": 1626425119,
            "email": "jenny.rosen@example.com",
            "individual": null,
            "livemode": false,
            "metadata": {},
            "name": "Jenny Rosen",
            "phone_number": "+18008675309",
            "redaction": null,
            "requirem
                stripe issuing authorizations retrieve iauth_1JVXl82eZvKYlo2CPIiWlzrn
            {
                "id": "iauth_1JVXl82eZvKYlo2CPIiWlzrn",
                "object": "issuing.authorization",
                "amount": 382,
                "amount_details": {
                    "atm_fee": null
                },
                "approved": false,
                "authorization_method": "online",
                "balance_transactions": [],
                "card": {
                    "id": "ic_1JDmgz2eZvKYlo2CRXlTsXj6",
                    "object": "issuing.card",
                    "brand": "Visa",
                    "cancellation_reason": null,
                    "cardholder": {
                        "id": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",
                        "object": "issuing.cardholder",
                        "billing": {
                            "address": {
                                "city": "San Francisco",
                                "country": "US",
                                "line1": "123 Main Street",
                                "line2": null,
                                "postal_code": "94111",
                                "state": "CA"
                            }
                        },
                        "company": null,
                        "created": 1626425119,
                        "email": "jenny.rosen@example.com",
                        "individual": null,
                        "livemode": false,
                        "metadata": {},
                        "name": "Jenny Rosen",
                        "phone_number": "+18008675309",
                        "redaction": null,
                        "requirem  },
                        "google_pay": {
                            "eligible": true,
                            "ineligible_reason": null
                        },
                        "primary_account_identifier": null
                    }
                },
                "cardholder": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",
                "created": 1630657706,
                "currency": "usd",
                "livemode": false,
                "merchant_amount": 382,
                "merchant_currency": "usd",
                "merchant_data": {
                    "category": "computer_software_stores",
                    "category_code": "5734",
                    "city": "SAN FRANCISCO",
                    "country": "US",
                    "name": "STRIPE",
                    "network_id": "1234567890",
                    "postal_code": "94103",
                    "state": "CA"
                },
                "metadata": {
                    "order_id": "6735"
                },
                "network_data": null,
                "pending_request": null,
                "redaction": null,
                "request_history": [
                    {
                        "amount": 382,
                        "amount_details": {
                            "atm_fee": null
                        },
                        "approved": false,
                        "created": 1630657706,
                        "currency": "usd",
                        "merchant_amount": 382,
                        "merchant_currency": "usd",
                        "reason": "verification_failed",
                        "
                            stripe issuing authorizations list \
                                                          - -limit = 3
{
    "object": "list",
    "url": "/v1/issuing/authorizations",
    "has_more": false,
    "data": [
        {
            "id": "iauth_1JVXl82eZvKYlo2CPIiWlzrn",
            "object": "issuing.authorization",
            "amount": 382,
            "amount_details": {
                "atm_fee": null
            },
            "approved": false,
            "authorization_method": "online",
            "balance_transactions": [],
            "card": {
                "id": "ic_1JDmgz2eZvKYlo2CRXlTsXj6",
                "object": "issuing.card",
                "brand": "Visa",
                "cancellation_reason": null,
                "cardholder": {
                    "id": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",
                    "object": "issuing.cardholder",
                    "billing": {
                        "address": {
                            "city": "San Francisco",
                            "country": "US",
                            "line1": "123 Main Street",
                            "line2": null,
                            "postal_code": "94111",
                            "state": "CA"
                        }
                    },
                    "company": null,
                    "created": 1626425119,
                    ble": true,
                       "ineligible_reason": null
},
"primary_account_identifier": null
}
},
"cardholder": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",
"created": 1630657706,
"currency": "usd",
"livemode": false,
"merchant_amount": 382,
"merchant_currency": "usd",
"merchant_data": {
    "category": "computer_software_stores",
    "category_code": "5734",
    "city": "SAN FRANCISCO",
    "country": "US",
    "name": "STRIPE",
    "network_id": "1234567890",
    "postal_code": "94103",
    "state": "CA"
},
"metadata": {
    "order_id": "6735"
},
"network_data": null,
"pending_request": null,
"redaction": null,
"request_history": [
    {
        "amount": 382,
        "amount_details": {
            "atm_fee": null
        },
        "approved": false,
        "created": 1630657706,
        "currency": "usd",
        "m
            stripe issuing authorizations approve iauth_1MvSKeLkdIwHu7ixKr8rO1HV
        {
            "id": "iauth_1MvSKeLkdIwHu7ixKr8rO1HV",
            "object": "issuing.authorization",
            "amount": 0,
            "amount_details": {
                "atm_fee": null
            },
            "approved": true,
            "authorization_method": "keyed_in",
            "balance_transactions": [],
            "card": {
                "id": "ic_1MvSKeLkdIwHu7ixFANTvxgn",
                "object": "issuing.card",
                "brand": "Visa",
                "cancellation_reason": null,
                "cardholder": {
                    "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",
                    "object": "issuing.cardholder",
                    "billing": {
                        "address": {
                            "city": "Anytown",
                            "country": "US",
                            "line1": "123 Main Street",
                            "line2": null,
                            "postal_code": "12345",
                            "state": "CA"
                        }
                    },
                    "company": null,
                    "created": 1680415995,
                    "email": null,
                    "individual": null,
                    "livemode": false,
                    "metadata": {},
                    "name": "John Doe",
                    "phone_number": null,
                    "requirements": {
                        "disabled_reason": "requirements.past_due",
                        xp_month": 8,
                                "exp_year": 2024,
        "last4": "4242",
        "livemode": false,
        "metadata": {},
        "replaced_by": null,
        "replacement_for": null,
        "replacement_reason": null,
        "shipping": null,
        "spending_controls": {
            "allowed_categories": null,
            "blocked_categories": null,
            "spending_limits": [],
            "spending_limits_currency": null
        },
        "status": "active",
        "type": "physical",
        "wallets": {
            "apple_pay": {
                "eligible": false,
                "ineligible_reason": "missing_cardholder_contact"
            },
            "google_pay": {
                "eligible": false,
                "ineligible_reason": "missing_cardholder_contact"
            },
            "primary_account_identifier": null
        }
    },
    "cardholder": null,
"created": 1681162380,
"currency": "usd",
"livemode": false,
"merchant_amount": 0,
"merchant_currency": "usd",
"merchant_data": {
    "category": "taxicabs_limousines",
    "category_code": "4121",
    "city": "San Francisco",
    stripe issuing authorizations decline iauth_1JVXl82eZvKYlo2CPIiWlzrn
        {
            "id": "iauth_1JVXl82eZvKYlo2CPIiWlzrn",
            "object": "issuing.authorization",
            "amount": 382,
            "amount_details": {
                "atm_fee": null
            },
            "approved": false,
            "authorization_method": "online",
            "balance_transactions": [],
            "card": {
                "id": "ic_1JDmgz2eZvKYlo2CRXlTsXj6",
                "object": "issuing.card",
                "brand": "Visa",
                "cancellation_reason": null,
                "cardholder": {
                    "id": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",
                    "object": "issuing.cardholder",
                    "billing": {
                        "address": {
                            "city": "San Francisco",
                            "country": "US",
                            "line1": "123 Main Street",
                            "line2": null,
                            "postal_code": "94111",
                            "state": "CA"
                        }
                    },
                    "company": null,
                    "created": 1626425119,
                    "email": "jenny.rosen@example.com",
                    "individual": null,
                    "livemode": false,
                    "metadata": {},
                    "name": "Jenny Rosen",
                    "phone_number": "+18008675309",
                    "redaction": null,
                    "requiremspending_limits_currency": "usd"
                },
                "status": "active",
                "type": "virtual",
                "wallets": {
                    "apple_pay": {
                        "eligible": true,
                        "ineligible_reason": null
                    },
                    "google_pay": {
                        "eligible": true,
                        "ineligible_reason": null
                    },
                    "primary_account_identifier": null
                }
            },
            "cardholder": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",
            "created": 1630657706,
            "currency": "usd",
            "livemode": false,
            "merchant_amount": 382,
            "merchant_currency": "usd",
            "merchant_data": {
                "category": "computer_software_stores",
                "category_code": "5734",
                "city": "SAN FRANCISCO",
                "country": "US",
                "name": "STRIPE",
                "network_id": "1234567890",
                "postal_code": "94103",
                "state": "CA"
            },
            "metadata": {
                "order_id": "6735"
            },
            "network_data": null,
            "pending_request": null,
            "redaction": null,
            "request_history": [
                {
                    "amount": 382,
                    "amount_details": {
                        "atm_fee": null
                    },
                    stripe test_helpers issuing authorizations create \
                                                               - -amount = 1000 \
                                                                           - -card = ic_1Nsse72eZvKYlo2CWBGm2WQ5
{
    "id": "iauth_1DPc772eZvKYlo2C6avLyZ25",
    "object": "issuing.authorization",
    "amount": 1000,
    "amount_details": {
        "atm_fee": null,
        "cashback_amount": null
    },
    "approved": true,
    "authorization_method": "keyed_in",
    "balance_transactions": [],
    "card": "ic_1Nsse72eZvKYlo2CWBGm2WQ5",
    "cardholder": "ich_1Ccy6F2eZvKYlo2ClnIm9bs4",
    "created": 1540586461,
    "currency": "usd",
    "livemode": false,
    "merchant_amount": 0,
    "merchant_currency": "usd",
    "merchant_data": {
        "category": "taxicabs_limousines",
        "category_code": "4121",
        "city": "San Francisco",
        "country": "US",
        "name": "Rocket Rides",
        "network_id": "1234567890",
        "postal_code": "94107",
        "state": "CA",
        "terminal_id": null
    },
    "metadata": {},
    "network_data": null,
    "pending_request": null,
    "redaction": null,
    "request_history": [],
    "status": "reversed",
    "transactions": [],
    "verification_data": {
        "address_line1_check": "not_provided",
        "addr
            stripe test_helpers issuing authorizations capture iauth_1DPc772eZvKYlo2C6avLyZ25
            {
                "id": "iauth_1DPc772eZvKYlo2C6avLyZ25",
                "object": "issuing.authorization",
                "amount": 0,
                "amount_details": {
                    "atm_fee": null,
                    "cashback_amount": null
                },
                "approved": true,
                "authorization_method": "keyed_in",
                "balance_transactions": [],
                "card": {
                    "id": "ic_1FEiQC2eZvKYlo2CtahKepKy",
                    "object": "issuing.card",
                    "brand": "Visa",
                    "cancellation_reason": null,
                    "cardholder": {
                        "id": "ich_1Ccy6F2eZvKYlo2ClnIm9bs4",
                        "object": "issuing.cardholder",
                        "billing": {
                            "address": {
                                "city": "Beverly Hills",
                                "country": "US",
                                "line1": "123 Fake St",
                                "line2": "Apt 3",
                                "postal_code": "90210",
                                "state": "CA"
                            }
                        },
                        "company": null,
                        "created": 1528992903,
                        "email": "jenny@example.com",
                        "individual": null,
                        "livemode": false,
                        "metadata": {},
                        "name": "Jenny Rosen",
                        "phone_number": "+18008675309",
                        "preferred_lo       "eligible": false,
                                                     "ineligible_reason": "missing_agreement"
                    },
                    "primary_account_identifier": null
                }
            },
        "cardholder": "ich_1Ccy6F2eZvKYlo2ClnIm9bs4",
        "created": 1540586461,
        "currency": "usd",
        "livemode": false,
        "merchant_amount": 0,
        "merchant_currency": "usd",
        "merchant_data": {
            "category": "taxicabs_limousines",
            "category_code": "4121",
            "city": "San Francisco",
            "country": "US",
            "name": "Rocket Rides",
            "network_id": "1234567890",
            "postal_code": "94107",
            "state": "CA",
            "terminal_id": null
        },
        "metadata": {},
        "network_data": null,
        "pending_request": null,
        "redaction": null,
        "request_history": [],
        "status": "reversed",
        "transactions": [],
        "verification_data": {
            "address_line1_check": "not_provided",
            "address_postal_code_check": "match",
            "cvc_check": "match",
            "expiry_check": "match"
        },
        "wallet": null
    }
    stripe test_helpers issuing authorizations expire iauth_1DPc772eZvKYlo2C6avLyZ25
    {
        "id": "iauth_1DPc772eZvKYlo2C6avLyZ25",
        "object": "issuing.authorization",
        "amount": 0,
        "amount_details": {
            "atm_fee": null,
            "cashback_amount": null
        },
        "approved": true,
        "authorization_method": "keyed_in",
        "balance_transactions": [],
        "card": {
            "id": "ic_1FEiQC2eZvKYlo2CtahKepKy",
            "object": "issuing.card",
            "brand": "Visa",
            "cancellation_reason": null,
            "cardholder": {
                "id": "ich_1Ccy6F2eZvKYlo2ClnIm9bs4",
                "object": "issuing.cardholder",
                "billing": {
                    "address": {
                        "city": "Beverly Hills",
                        "country": "US",
                        "line1": "123 Fake St",
                        "line2": "Apt 3",
                        "postal_code": "90210",
                        "state": "CA"
                    }
                },
                "company": null,
                "created": 1528992903,
                "email": "jenny@example.com",
                "individual": null,
                "livemode": false,
                "metadata": {},
                "name": "Jenny Rosen",
                "phone_number": "+18008675309",
                "preferred_lolacement_for": null,
                "replacement_reason": null,
                "shipping": null,
                "spending_controls": {
                    "allowed_categories": null,
                    "blocked_categories": null,
                    "spending_limits": [],
                    "spending_limits_currency": null
                },
                "status": "canceled",
                "type": "physical",
                "wallets": {
                    "apple_pay": {
                        "eligible": true,
                        "ineligible_reason": null
                    },
                    "google_pay": {
                        "eligible": false,
                        "ineligible_reason": "missing_agreement"
                    },
                    "primary_account_identifier": null
                }
            },
            "cardholder": "ich_1Ccy6F2eZvKYlo2ClnIm9bs4",
            "created": 1540586461,
            "currency": "usd",
            "livemode": false,
            "merchant_amount": 0,
            "merchant_currency": "usd",
            "merchant_data": {
                "category": "taxicabs_limousines",
                "category_code": "4121",
                "city": "San Francisco",
                "country": "US",
                "name": "Rocket Rides",
                "network_id": "1234567890",
                "postal_code": "94107",
                "state": "CA",
                "termi
                    stripe test_helpers issuing authorizations finalize_amount iauth_1DPc772eZvKYlo2C6avLyZ25 \
                                                                               - -final - amount = 1000
{
    "id": "iauth_1DPc772eZvKYlo2C6avLyZ25",
    "object": "issuing.authorization",
    "amount": 1000,
    "amount_details": {
        "atm_fee": null,
        "cashback_amount": null
    },
    "approved": true,
    "authorization_method": "chip",
    "balance_transactions": [],
    "card": "ic_1Nsse72eZvKYlo2CWBGm2WQ5",
    "cardholder": "ich_1Ccy6F2eZvKYlo2ClnIm9bs4",
    "created": 1540586461,
    "currency": "usd",
    "livemode": false,
    "merchant_amount": 1000,
    "merchant_currency": "usd",
    "merchant_data": {
        "category": "automated_fuel_dispensers",
        "category_code": "5542",
        "city": "San Francisco",
        "country": "US",
        "name": "Rocket Rides",
        "network_id": "1234567890",
        "postal_code": "94107",
        "state": "CA",
        "terminal_id": null
    },
    "metadata": {},
    "network_data": null,
    "pending_request": null,
    "redaction": null,
    "request_history": [],
    "status": "reversed",
    "transactions": [],
    "verification_data": {
        "address_line1_check": "not_provided",

        curl https: // api.stripe.com / v1 / test_helpers / issuing / authorizations / iauth_1JVXl82eZvKYlo2CPIiWlzrn / fraud_challenges / respond \
                       - u
"sk_test_ESDdbUTrLo4e9SC7uoQqlhd2:" \
- d
confirmed = true

{
    "id": "iauth_1JVXl82eZvKYlo2CPIiWlzrn",
    "object": "issuing.authorization",
    "amount": 382,
    "amount_details": {
        "atm_fee": null
    },
    "approved": false,
    "authorization_method": "online",
    "balance_transactions": [],
    "card": {
        "id": "ic_1JDmgz2eZvKYlo2CRXlTsXj6",
        "object": "issuing.card",
        "brand": "Visa",
        "cancellation_reason": null,
        "cardholder": {
            "id": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",
            "object": "issuing.cardholder",
            "billing": {
                "address": {
                    "city": "San Francisco",
                    "country": "US",
                    "line1": "123 Main Street",
                    "line2": null,
                    "postal_code": "94111",
                    "state": "CA"
                }
            },
            "company": null,
            "created": 1626425119,
            "email": "jenny.rosen@example.com",
            "individual": null,
            "livemode": false,
            "metadata": {},
            "name": "Jenny Rosen",
            "phone_number": "+18008675309",
            "redaction": null,
            "requirem  },
            "google_pay": {
                "eligible": true,
                "ineligible_reason": null
            },
            "primary_account_identifier": null
        }
    },
    "cardholder": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",
    "created": 1630657706,
    "currency": "usd",
    "livemode": false,
    "merchant_amount": 382,
    "merchant_currency": "usd",
    "merchant_data": {
        "category": "computer_software_stores",
        "category_code": "5734",
        "city": "SAN FRANCISCO",
        "country": "US",
        "name": "STRIPE",
        "network_id": "1234567890",
        "postal_code": "94103",
        "state": "CA"
    },
    "metadata": {
        "order_id": "6735"
    },
    "network_data": null,
    "pending_request": null,
    "redaction": null,
    "request_history": [
        {
            "amount": 382,
            "amount_details": {
                "atm_fee": null
            },
            "approved": false,
            "created": 1630657706,
            "currency": "usd",
            "merchant_amount": 382,
            "merchant_currency": "usd",
            "reason": "verification_failed",
            "
                stripe test_helpers issuing authorizations reverse iauth_1DPc772eZvKYlo2C6avLyZ25
            {
                "id": "iauth_1DPc772eZvKYlo2C6avLyZ25",
                "object": "issuing.authorization",
                "amount": 0,
                "amount_details": {
                    "atm_fee": null,
                    "cashback_amount": null
                },
                "approved": true,
                "authorization_method": "keyed_in",
                "balance_transactions": [],
                "card": {
                    "id": "ic_1FEiQC2eZvKYlo2CtahKepKy",
                    "object": "issuing.card",
                    "brand": "Visa",
                    "cancellation_reason": null,
                    "cardholder": {
                        "id": "ich_1Ccy6F2eZvKYlo2ClnIm9bs4",
                        "object": "issuing.cardholder",
                        "billing": {
                            "address": {
                                "city": "Beverly Hills",
                                "country": "US",
                                "line1": "123 Fake St",
                                "line2": "Apt 3",
                                "postal_code": "90210",
                                "state": "CA"
                            }
                        },
                        "company": null,
                        "created": 1528992903,
                        "email": "jenny@example.com",
                        "individual": null,
                        "livemode": false,
                        "metadata": {},
                        "name": "Jenny Rosen",
                        "phone_number": "+18008675309",
                        "preferred_lopping": null,
                        "spending_controls": {
                            "allowed_categories": null,
                            "blocked_categories": null,
                            "spending_limits": [],
                            "spending_limits_currency": null
                        },
                        "status": "canceled",
                        "type": "physical",
                        "wallets": {
                            "apple_pay": {
                                "eligible": true,
                                "ineligible_reason": null
                            },
                            "google_pay": {
                                "eligible": false,
                                "ineligible_reason": "missing_agreement"
                            },
                            "primary_account_identifier": null
                        }
                    },
                    "cardholder": "ich_1Ccy6F2eZvKYlo2ClnIm9bs4",
                    "created": 1540586461,
                    "currency": "usd",
                    "livemode": false,
                    "merchant_amount": 0,
                    "merchant_currency": "usd",
                    "merchant_data": {
                        "category": "taxicabs_limousines",
                        "category_code": "4121",
                        "city": "San Francisco",
                        "country": "US",
                        "name": "Rocket Rides",
                        "network_id": "1234567890",
                        "postal_code": "94107",
                        "state": "CA",
                        "terminal_id": null
                    },
                    "metadata": {},
                    "network_data": null,
                    {
                        "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",
                        "object": "issuing.cardholder",
                        "billing": {
                            "address": {
                                "line1": "1234 Main Street",
                                "city": "San Francisco",
                                "state": "CA",
                                "country": "US",
                                "postal_code": "94111"
                            }
                        },
                        "company": null,
                        "created": 1680415995,
                        "email": "jenny.rosen@example.com",
                        "individual": null,
                        "livemode": false,
                        "metadata": {},
                        "name": "Jenny Rosen",
                        "phone_number": "+18888675309",
                        "redaction": null,
                        "requirements": {
                            "disabled_reason": "requirements.past_due",
                            "past_due": [
                                "individual.card_issuing.user_terms_acceptance.ip",
                                "individual.card_issuing.user_terms_acceptance.date",
                                "individual.first_name",
                                "individual.last_name"
                            ]
                        },
                        "spending_controls": {
                            "allowed_categories": [],
                            "blocked_categories": [],
                            "spending_limits": [],
                            "spending_limits_currency": null
                        },
                        "status": "active",
                        "type": "individual"
                    }
                        stripe issuing cardholders create \
                                                   - -type = individual \
                                                             - -name = "Jenny Rosen" \
                                                                       - -email = "jenny.rosen@example.com" \
                                                                                  - -phone - number = "+18888675309" \
                                                                                                      - d
"billing[address][line1]" = "1234 Main Street" \
                            - d
"billing[address][city]" = "San Francisco" \
                           - d
"billing[address][state]" = CA \
                            - d
"billing[address][country]" = US \
                              - d
"billing[address][postal_code]" = 94111

{
    "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",
    "object": "issuing.cardholder",
    "billing": {
        "address": {
            "line1": "1234 Main Street",
            "city": "San Francisco",
            "state": "CA",
            "country": "US",
            "postal_code": "94111"
        }
    },
    "company": null,
    "created": 1680415995,
    "email": "jenny.rosen@example.com",
    "individual": null,
    "livemode": false,
    "metadata": {},
    "name": "Jenny Rosen",
    "phone_number": "+18888675309",
    "redaction": null,
    "requirements": {
        "disabled_reason": "requirements.past_due",
        "past_due": [
            "individual.card_issuing.user_terms_acceptance.ip",
            "individual.card_issuing.user_terms_acceptance.date",
            "individual.first_name",
            "individual.last_name"
        ]
    },
    "spending_controls": {
        "allowed_categories": [],
        "blocked_categories": [],
        "spending_limits": [],
        "spending_limits_currency": null
    },
    "status": "active",
    "type": "individual"
}

stripe
issuing
cardholders
update
ich_1MsKAB2eZvKYlo2C3eZ2BdvK \
- d
"metadata[order_id]" = 6735
{
    "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",
    "object": "issuing.cardholder",
    "billing": {
        "address": {
            "line1": "1234 Main Street",
            "city": "San Francisco",
            "state": "CA",
            "country": "US",
            "postal_code": "94111"
        }
    },
    "company": null,
    "created": 1680415995,
    "email": "jenny.rosen@example.com",
    "individual": null,
    "livemode": false,
    "metadata": {
        "order_id": "6735"
    },
    "name": "Jenny Rosen",
    "phone_number": "+18888675309",
    "redaction": null,
    "requirements": {
        "disabled_reason": "requirements.past_due",
        "past_due": [
            "individual.card_issuing.user_terms_acceptance.ip",
            "individual.card_issuing.user_terms_acceptance.date",
            "individual.first_name",
            "individual.last_name"
        ]
    },
    "spending_controls": {
        "allowed_categories": [],
        "blocked_categories": [],
        "spending_limits": [],
        "spending_limits_currency": null
    },
    "status": "active",
    "type": "individual"
}

stripe
issuing
cardholders
retrieve
ich_1MsKAB2eZvKYlo2C3eZ2BdvK
{
    "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",
    "object": "issuing.cardholder",
    "billing": {
        "address": {
            "line1": "1234 Main Street",
            "city": "San Francisco",
            "state": "CA",
            "country": "US",
            "postal_code": "94111"
        }
    },
    "company": null,
    "created": 1680415995,
    "email": "jenny.rosen@example.com",
    "individual": null,
    "livemode": false,
    "metadata": {},
    "name": "Jenny Rosen",
    "phone_number": "+18888675309",
    "redaction": null,
    "requirements": {
        "disabled_reason": "requirements.past_due",
        "past_due": [
            "individual.card_issuing.user_terms_acceptance.ip",
            "individual.card_issuing.user_terms_acceptance.date",
            "individual.first_name",
            "individual.last_name"
        ]
    },
    "spending_controls": {
        "allowed_categories": [],
        "blocked_categories": [],
        "spending_limits": [],
        "spending_limits_currency": null
    },
    "status": "active",
    "type": "individual"
}
{
    "object": "list",
    "url": "/v1/issuing/cardholders",
    "has_more": false,
    "data": [
        {
            "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",
            "object": "issuing.cardholder",
            "billing": {
                "address": {
                    "line1": "1234 Main Street",
                    "city": "San Francisco",
                    "state": "CA",
                    "country": "US",
                    "postal_code": "94111"
                }
            },
            "company": null,
            "created": 1680415995,
            "email": "jenny.rosen@example.com",
            "individual": null,
            "livemode": false,
            "metadata": {},
            "name": "Jenny Rosen",
            "phone_number": "+18888675309",
            "redaction": null,
            "requirements": {
                "disabled_reason": "requirements.past_due",
                "past_due": [
                    "individual.card_issuing.user_terms_acceptance.ip",
                    "individual.card_issuing.user_terms_acceptance.date",
                    "individual.first_name",
                    "individual.last_name"
                ]
            },
            "spending_contro
                {
                    "id": "ic_1MvSieLkdIwHu7ixn6uuO0Xu",
                    "object": "issuing.card",
                    "brand": "Visa",
                    "cancellation_reason": null,
                    "cardholder": {
                        "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",
                        "object": "issuing.cardholder",
                        "billing": {
                            "address": {
                                "city": "Anytown",
                                "country": "US",
                                "line1": "123 Main Street",
                                "line2": null,
                                "postal_code": "12345",
                                "state": "CA"
                            }
                        },
                        "company": null,
                        "created": 1680415995,
                        "email": null,
                        "individual": null,
                        "livemode": false,
                        "metadata": {},
                        "name": "John Doe",
                        "phone_number": null,
                        "requirements": {
                            "disabled_reason": "requirements.past_due",
                            "past_due": [
                                "individual.card_issuing.user_terms_acceptance.ip",
                                "individual.card_issuing.user_terms_acceptance.date",
                                "individual.first_name",
                                "individual.last_name"
                            ]
                        },
                        "spending_controls": {
                            "allowed_categories": [],
                            "blocked_categ
                                stripe issuing cards create \
                                                     - -cardholder = ich_1MsKAB2eZvKYlo2C3eZ2BdvK \
                                                                     - -currency = usd \
                                                                                   - -type = virtual
{
    "id": "ic_1MvSieLkdIwHu7ixn6uuO0Xu",
    "object": "issuing.card",
    "brand": "Visa",
    "cancellation_reason": null,
    "cardholder": {
        "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",
        "object": "issuing.cardholder",
        "billing": {
            "address": {
                "city": "Anytown",
                "country": "US",
                "line1": "123 Main Street",
                "line2": null,
                "postal_code": "12345",
                "state": "CA"
            }
        },
        "company": null,
        "created": 1680415995,
        "email": null,
        "individual": null,
        "livemode": false,
        "metadata": {},
        "name": "John Doe",
        "phone_number": null,
        "requirements": {
            "disabled_reason": "requirements.past_due",
            "past_due": [
                "individual.card_issuing.user_terms_acceptance.ip",
                "individual.card_issuing.user_terms_acceptance.date",
                "individual.first_name",
                "individual.last_name"
            ]
        },
        "spending_controls": {
            "allowed_categories": [],
            "blocked_categes": null,
            "blocked_categories": null,
            "spending_limits": [],
            "spending_limits_currency": null
        },
        "status": "active",
        "type": "virtual",
        "wallets": {
            "apple_pay": {
                "eligible": false,
                "ineligible_reason": "missing_cardholder_contact"
            },
            "google_pay": {
                "eligible": false,
                "ineligible_reason": "missing_cardholder_contact"
            },
            "primary_account_identifier": null
        }
    }
    stripe issuing cards update ic_1MvSieLkdIwHu7ixn6uuO0Xu \
                                - d "metadata[order_id]" = 6735
{
    "id": "ic_1MvSieLkdIwHu7ixn6uuO0Xu",
    "object": "issuing.card",
    "brand": "Visa",
    "cancellation_reason": null,
    "cardholder": {
        "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",
        "object": "issuing.cardholder",
        "billing": {
            "address": {
                "city": "Anytown",
                "country": "US",
                "line1": "123 Main Street",
                "line2": null,
                "postal_code": "12345",
                "state": "CA"
            }
        },
        "company": null,
        "created": 1680415995,
        "email": null,
        "individual": null,
        "livemode": false,
        "metadata": {},
        "name": "John Doe",
        "phone_number": null,
        "requirements": {
            "disabled_reason": "requirements.past_due",
            "past_due": [
                "individual.card_issuing.user_terms_acceptance.ip",
                "individual.card_issuing.user_terms_acceptance.date",
                "individual.first_name",
                "individual.last_name"
            ]
        },
        "spending_controls": {
            "allowed_categories": [],
            "blocked_categ
                stripe issuing cards retrieve ic_1MvSieLkdIwHu7ixn6uuO0Xu
            {
                "id": "ic_1MvSieLkdIwHu7ixn6uuO0Xu",
                "object": "issuing.card",
                "brand": "Visa",
                "cancellation_reason": null,
                "cardholder": {
                    "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",
                    "object": "issuing.cardholder",
                    "billing": {
                        "address": {
                            "city": "Anytown",
                            "country": "US",
                            "line1": "123 Main Street",
                            "line2": null,
                            "postal_code": "12345",
                            "state": "CA"
                        }
                    },
                    "company": null,
                    "created": 1680415995,
                    "email": null,
                    "individual": null,
                    "livemode": false,
                    "metadata": {},
                    "name": "John Doe",
                    "phone_number": null,
                    "requirements": {
                        "disabled_reason": "requirements.past_due",
                        "past_due": [
                            "individual.card_issuing.user_terms_acceptance.ip",
                            "individual.card_issuing.user_terms_acceptance.date",
                            "individual.first_name",
                            "individual.last_name"
                        ]
                    },
                    "spending_controls": {
                        "allowed_categories": [],
                        "blocked_categl",
                    "wallets": {
                        "apple_pay": {
                            "eligible": false,
                            "ineligible_reason": "missing_cardholder_contact"
                        },
                        "google_pay": {
                            "eligible": false,
                            "ineligible_reason": "missing_cardholder_contact"
                        },
                        "primary_account_identifier": null
                    }
                }

                stripe issuing cards list \
                                     - -limit = 3

{
    "object": "list",
    "url": "/v1/issuing/cards",
    "has_more": false,
    "data": [
        {
            "id": "ic_1MvSieLkdIwHu7ixn6uuO0Xu",
            "object": "issuing.card",
            "brand": "Visa",
            "cancellation_reason": null,
            "cardholder": {
                "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",
                "object": "issuing.cardholder",
                "billing": {
                    "address": {
                        "city": "Anytown",
                        "country": "US",
                        "line1": "123 Main Street",
                        "line2": null,
                        "postal_code": "12345",
                        "state": "CA"
                    }
                },
                "company": null,
                "created": 1680415995,
                "email": null,
                "individual": null,
                "livemode": false,
                "metadata": {},
                "name": "John Doe",
                "phone_number": null,
                "requirements": {
                    "disabled_reason": "requirements.past_due",
                    "past_due": [
                        "individual.card_issuing.user_terms_acceptance.ip",
                        "indiblocked_categories": [],
"spending_limits": [],
"spending_limits_currency": null
},
"status": "active",
"type": "individual"
},
"created": 1681163868,
"currency": "usd",
"exp_month": 8,
"exp_year": 2024,
"last4": "4242",
"livemode": false,
"metadata": {},
"replaced_by": null,
"replacement_for": null,
"replacement_reason": null,
"shipping": null,
"spending_controls": {
    "allowed_categories": null,
    "blocked_categories": null,
    "spending_limits": [],
    "spending_limits_currency": null
},
"status": "active",
"type": "virtual",
"wallets": {
    "apple_pay": {
        "eligible": false,
        "ineligible_reason": "missing_cardholder_contact"
    },
    "google_pay": {
        "eligible": false,
        "ineligible_reason": "missing_cardholder_contact"
    },
    "primary_account_i
        {
            "id": "ipcd_Oiw9GXcFRE81LZ",
            "object": "issuing.personalization_design",
            "livemode": true,
            "card_logo": "file_1LzR9L2eZvKYlo2CelTpcvKu",
            "carrier_text": null,
            "lookup_key": "my_card_design_lookup_key",
            "metadata": {},
            "name": "My personalization design name",
            "physical_bundle": "ics_Oiw9ahglMfql0U",
            "preferences": {
                "is_default": false
            },
            "rejection_reasons": {
                "card_logo": [],
                "carrier_text": []
            },
            "status": "review"
        }
    stripe issuing personalization_designs create \
                                           - -name = "My personalization design name" \
                                                     - d
"preferences[is_default]" = false \
                            - -card - logo = file_1LzR9L2eZvKYlo2CelTpcvKu \
                                             - -physical - bundle = ics_Oiw9ahglMfql0U
{
    "id": "ipcd_Oiw9GXcFRE81LZ",
    "object": "issuing.personalization_design",
    "livemode": true,
    "card_logo": "file_1LzR9L2eZvKYlo2CelTpcvKu",
    "carrier_text": null,
    "lookup_key": "my_card_design_lookup_key",
    "metadata": {},
    "name": "My personalization design name",
    "physical_bundle": "ics_Oiw9ahglMfql0U",
    "preferences": {
        "is_default": false
    },
    "rejection_reasons": {
        "card_logo": [],
        "carrier_text": []
    },
    "status": "review"
}
stripe
issuing
personalization_designs
update
ipcd_Oiw9GXcFRE81LZ \
- d
"metadata[order_id]" = 6735
{
    "id": "ipcd_Oiw9GXcFRE81LZ",
    "object": "issuing.personalization_design",
    "livemode": true,
    "card_logo": "file_1LzR9L2eZvKYlo2CelTpcvKu",
    "carrier_text": null,
    "lookup_key": "my_card_design_lookup_key",
    "metadata": {
        "order_id": "6735"
    },
    "name": "My personalization design name",
    "physical_bundle": "ics_Oiw9ahglMfql0U",
    "preferences": {
        "is_default": false
    },
    "rejection_reasons": {
        "card_logo": [],
        "carrier_text": []
    },
    "status": "review"
}
stripe
issuing
personalization_designs
retrieve
ipcd_Oiw9GXcFRE81LZ
{
    "id": "ipcd_Oiw9GXcFRE81LZ",
    "object": "issuing.personalization_design",
    "livemode": true,
    "card_logo": "file_1LzR9L2eZvKYlo2CelTpcvKu",
    "carrier_text": null,
    "lookup_key": "my_card_design_lookup_key",
    "metadata": {},
    "name": "My personalization design name",
    "physical_bundle": "ics_Oiw9ahglMfql0U",
    "preferences": {
        "is_default": false
    },
    "rejection_reasons": {
        "card_logo": [],
        "carrier_text": []
    },
    "status": "review"
}
stripe
issuing
personalization_designs
list \
- -limit = 3
{
    "object": "list",
    "url": "/v1/issuing/personalization_designs",
    "has_more": false,
    "data": [
        {
            "id": "ipcd_Oiw9GXcFRE81LZ",
            "object": "issuing.personalization_design",
            "livemode": true,
            "card_logo": "file_1LzR9L2eZvKYlo2CelTpcvKu",
            "carrier_text": null,
            "lookup_key": "my_card_design_lookup_key",
            "metadata": {},
            "name": "My personalization design name",
            "physical_bundle": "ics_Oiw9ahglMfql0U",
            "preferences": {
                "is_default": false
            },
            "rejection_reasons": {
                "card_logo": [],
                "carrier_text": []
            },
            "status": "review"
        }
        {...}
        {...}
    ],
}
stripe
test_helpers
issuing
personalization_designs
activate
ipcd_Oiw9GXcFRE81LZ
{
    "id": "ipcd_Oiw9GXcFRE81LZ",
    "object": "issuing.personalization_design",
    "livemode": false,
    "card_logo": "file_1LzR9L2eZvKYlo2CelTpcvKu",
    "carrier_text": null,
    "lookup_key": "my_card_design_lookup_key",
    "metadata": {},
    "name": "My personalization design name",
    "physical_bundle": "ics_Oiw9ahglMfql0U",
    "preferences": {
        "is_default": false
    },
    "rejection_reasons": {
        "card_logo": [],
        "carrier_text": []
    },
    "status": "active"
}
stripe
test_helpers
issuing
personalization_designs
deactivate
ipcd_Oiw9GXcFRE81LZ
{
    "id": "intok_1MzDbE2eZvKYlo2C26a98MDg",
    "object": "issuing.token",
    "card": "ic_1MytUz2eZvKYlo2CZCn5fuvZ",
    "created": 1682059060,
    "network_updated_at": 1682059060,
    "livemode": false,
    "status": "active",
    "last4": "2424",
    "token_service_provider": "visa",
    "wallet_provider": "apple_pay",
    "device_fingerprint": "intd_1MzDbE2eZvKYcp3095svdf"
}
stripe
issuing
tokens
update
intok_1MzDbE2eZvKYlo2C26a98MDg \
- -status = suspended
{
    "id": "intok_1MzDbE2eZvKYlo2C26a98MDg",
    "object": "issuing.token",
    "card": "ic_1MytUz2eZvKYlo2CZCn5fuvZ",
    "created": 1682059060,
    "network_updated_at": 1682059060,
    "livemode": false,
    "status": "suspended",
    "last4": "2424",
    "token_service_provider": "visa",
    "wallet_provider": "apple_pay",
    "device_fingerprint": "intd_1MzDbE2eZvKYcp3095svdf"
}
stripe
issuing
tokens
retrieve
intok_1MzDbE2eZvKYlo2C26a98MDg
{
    "id": "intok_1MzDbE2eZvKYlo2C26a98MDg",
    "object": "issuing.token",
    "card": "ic_1MytUz2eZvKYlo2CZCn5fuvZ",
    "created": 1682059060,
    "network_updated_at": 1682059060,
    "livemode": false,
    "status": "active",
    "last4": "2424",
    "token_service_provider": "visa",
    "wallet_provider": "apple_pay",
    "device_fingerprint": "intd_1MzDbE2eZvKYcp3095svdf"
}
stripe
issuing
tokens
list \
- -limit = 3 \
           - -card = ic_1MytUz2eZvKYlo2CZCn5fuvZ
{
    "object": "list",
    "url": "/v1/issuing/tokens",
    "has_more": false,
    "data": [
        {
            "id": "intok_1MzDbE2eZvKYlo2C26a98MDg",
            "object": "issuing.token",
            "card": "ic_1MytUz2eZvKYlo2CZCn5fuvZ",
            "created": 1682059060,
            "network_updated_at": 1682059060,
            "livemode": false,
            "status": "suspended",
            "last4": "2424",
            "token_service_provider": "visa",
            "wallet_provider": "apple_pay",
            "device_fingerprint": "intd_1MzDbE2eZvKYcp3095svdf"
        }
        {...}
        {...}
    ],
}
{
    "id": "ipi_1MzFN1K8F4fqH0lBmFq8CjbU",
    "object": "issuing.transaction",
    "amount": -100,
    "amount_details": {
        "atm_fee": null
    },
    "authorization": "iauth_1MzFMzK8F4fqH0lBc9VdaZUp",
    "balance_transaction": "txn_1MzFN1K8F4fqH0lBQPtqUmJN",
    "card": "ic_1MzFMxK8F4fqH0lBjIUITRYi",
    "cardholder": "ich_1MzFMxK8F4fqH0lBXnFW0ROG",
    "created": 1682065867,
    "currency": "usd",
    "dispute": null,
    "livemode": false,
    "merchant_amount": -100,
    "merchant_currency": "usd",
    "merchant_data": {
        "category": "computer_software_stores",
        "category_code": "5734",
        "city": "SAN FRANCISCO",
        "country": "US",
        "name": "WWWW.BROWSEBUG.BIZ",
        "network_id": "1234567890",
        "postal_code": "94103",
        "state": "CA"
    },
    "metadata": {},
    "type": "capture",
    "wallet": null
}
stripe
issuing
transactions
update
ipi_1MzFN1K8F4fqH0lBmFq8CjbU \
- d
"metadata[order_id]" = 6735
{
    "id": "ipi_1MzFN1K8F4fqH0lBmFq8CjbU",
    "object": "issuing.transaction",
    "amount": -100,
    "amount_details": {
        "atm_fee": null
    },
    "authorization": "iauth_1MzFMzK8F4fqH0lBc9VdaZUp",
    "balance_transaction": "txn_1MzFN1K8F4fqH0lBQPtqUmJN",
    "card": "ic_1MzFMxK8F4fqH0lBjIUITRYi",
    "cardholder": "ich_1MzFMxK8F4fqH0lBXnFW0ROG",
    "created": 1682065867,
    "currency": "usd",
    "dispute": null,
    "livemode": false,
    "merchant_amount": -100,
    "merchant_currency": "usd",
    "merchant_data": {
        "category": "computer_software_stores",
        "category_code": "5734",
        "city": "SAN FRANCISCO",
        "country": "US",
        "name": "WWWW.BROWSEBUG.BIZ",
        "network_id": "1234567890",
        "postal_code": "94103",
        "state": "CA"
    },
    "metadata": {
        "order_id": "6735"
    },
    "type": "capture",
    "wallet": null
}

stripe
issuing
transactions
retrieve
ipi_1MzFN1K8F4fqH0lBmFq8CjbU
{
    "id": "ipi_1MzFN1K8F4fqH0lBmFq8CjbU",
    "object": "issuing.transaction",
    "amount": -100,
    "amount_details": {
        "atm_fee": null
    },
    "authorization": "iauth_1MzFMzK8F4fqH0lBc9VdaZUp",
    "balance_transaction": "txn_1MzFN1K8F4fqH0lBQPtqUmJN",
    "card": "ic_1MzFMxK8F4fqH0lBjIUITRYi",
    "cardholder": "ich_1MzFMxK8F4fqH0lBXnFW0ROG",
    "created": 1682065867,
    "currency": "usd",
    "dispute": null,
    "livemode": false,
    "merchant_amount": -100,
    "merchant_currency": "usd",
    "merchant_data": {
        "category": "computer_software_stores",
        "category_code": "5734",
        "city": "SAN FRANCISCO",
        "country": "US",
        "name": "WWWW.BROWSEBUG.BIZ",
        "network_id": "1234567890",
        "postal_code": "94103",
        "state": "CA"
    },
    "metadata": {},
    "type": "capture",
    "wallet": null
}
stripe
issuing
transactions
list \
- -limit = 3
{
    "object": "list",
    "url": "/v1/issuing/transactions",
    "has_more": false,
    "data": [
        {
            "id": "ipi_1MzFN1K8F4fqH0lBmFq8CjbU",
            "object": "issuing.transaction",
            "amount": -100,
            "amount_details": {
                "atm_fee": null
            },
            "authorization": "iauth_1MzFMzK8F4fqH0lBc9VdaZUp",
            "balance_transaction": "txn_1MzFN1K8F4fqH0lBQPtqUmJN",
            "card": "ic_1MzFMxK8F4fqH0lBjIUITRYi",
            "cardholder": "ich_1MzFMxK8F4fqH0lBXnFW0ROG",
            "created": 1682065867,
            "currency": "usd",
            "dispute": null,
            "livemode": false,
            "merchant_amount": -100,
            "merchant_currency": "usd",
            "merchant_data": {
                "category": "computer_software_stores",
                "category_code": "5734",
                "city": "SAN FRANCISCO",
                "country": "US",
                "name": "WWWW.BROWSEBUG.BIZ",
                "network_id": "1234567890",
                "postal_code": "94103",
                "state": "CA"
            },
            "metadata": {},
            "type": "capture",
            {
                "object": "terminal.connection_token",
                "secret": "pst_test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LE81ZEdIalZ6NlVuMUdjM3c3WkRnN0ZYRHZxRURwTXo_00gNK2DWAV"
            }
                stripe terminal connection_tokens create
            {
                "object": "terminal.connection_token",
                "secret": "pst_test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LE81ZEdIalZ6NlVuMUdjM3c3WkRnN0ZYRHZxRURwTXo_00gNK2DWAV"
            }
            {
                "id": "tml_FBakXQG8bQk4Mm",
                "object": "terminal.location",
                "address": {
                    "city": "San Francisco",
                    "country": "US",
                    "line1": "1234 Main Street",
                    "line2": "",
                    "postal_code": "94111",
                    "state": "CA"
                },
                "display_name": "My First Store",
                "livemode": false,
                "metadata": {}
            }
                stripe terminal locations create \
                                          - -display - name = "My First Store" \
                                                              - d
"address[line1]" = "1234 Main Street" \
                   - d
"address[city]" = "San Francisco" \
                  - d
"address[postal_code]" = 94111 \
                         - d
"address[state]" = CA \
                   - d
"address[country]" = US
{
    "id": "tml_FBakXQG8bQk4Mm",
    "object": "terminal.location",
    "address": {
        "city": "San Francisco",
        "country": "US",
        "line1": "1234 Main Street",
        "line2": "",
        "postal_code": "94111",
        "state": "CA"
    },
    "display_name": "My First Store",
    "livemode": false,
    "metadata": {}
}
stripe
terminal
locations
update
tml_FBakXQG8bQk4Mm \
- -display - name = "Update Store Name"
{
    "id": "tml_FBakXQG8bQk4Mm",
    "object": "terminal.location",
    "address": {
        "city": "San Francisco",
        "country": "US",
        "line1": "1234 Main Street",
        "line2": "",
        "postal_code": "94111",
        "state": "CA"
    },
    "display_name": "Update Store Name",
    "livemode": false,
    "metadata": {}
}
stripe
terminal
locations
retrieve
tml_FBakXQG8bQk4Mm
{
    "id": "tml_FBakXQG8bQk4Mm",
    "object": "terminal.location",
    "address": {
        "city": "San Francisco",
        "country": "US",
        "line1": "1234 Main Street",
        "line2": "",
        "postal_code": "94111",
        "state": "CA"
    },
    "display_name": "My First Store",
    "livemode": false,
    "metadata": {}
}
stripe
terminal
locations
list \
- -limit = 3
{
    "object": "list",
    "url": "/v1/terminal/locations",
    "has_more": false,
    "data": [
        {
            "id": "tml_FBakXQG8bQk4Mm",
            "object": "terminal.location",
            "address": {
                "city": "San Francisco",
                "country": "US",
                "line1": "1234 Main Street",
                "line2": "",
                "postal_code": "94111",
                "state": "CA"
            },
            "display_name": "My First Store",
            "livemode": false,
            "metadata": {}
        }
        {...}
        {...}
    ],
}
{
    "id": "rc_1MtkSr2eZvKYlo2CcysvUbEw",
    "object": "treasury.received_credit",
    "amount": 1000,
    "created": 1680755425,
    "currency": "usd",
    "description": "Stripe Test",
    "failure_code": null,
    "financial_account": "fa_1MtkSr2eZvKYlo2CsJozwFWD",
    "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOKVuaEGMgagXvSInCY6NpMvimqdsEKNHRrHZ3OGyVm_l5LfDMezNeY83F5Mq-rryXZ-J1z-jfFBv30wz5WxDH97VRBIzw",
    "initiating_payment_method_details": {
        "billing_details": {
            "address": {
                "city": null,
                "country": null,
                "line1": null,
                "line2": null,
                "postal_code": null,
                "state": null
            },
            "email": null,
            "name": "Jane Austen"
        },
        "type": "us_bank_account",
        "us_bank_account": {
            "bank_name": "STRIPE TEST BANK",
            "last4": "6789",
            "routing_number": "110000000"
        }
    },
    "linked_flows": {
        "credit_reversal": null,
        "issuing_
            {
                "id": "rc_1MtkSr2eZvKYlo2CcysvUbEw",
                "object": "treasury.received_credit",
                "amount": 1000,
                "created": 1680755425,
                "currency": "usd",
                "description": "Stripe Test",
                "failure_code": null,
                "financial_account": "fa_1MtkSr2eZvKYlo2CsJozwFWD",
                "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOKVuaEGMgagXvSInCY6NpMvimqdsEKNHRrHZ3OGyVm_l5LfDMezNeY83F5Mq-rryXZ-J1z-jfFBv30wz5WxDH97VRBIzw",
                "initiating_payment_method_details": {
                    "billing_details": {
                        "address": {
                            "city": null,
                            "country": null,
                            "line1": null,
                            "line2": null,
                            "postal_code": null,
                            "state": null
                        },
                        "email": null,
                        "name": "Jane Austen"
                    },
                    "type": "us_bank_account",
                    "us_bank_account": {
                        "bank_name": "STRIPE TEST BANK",
                        "last4": "6789",
                        "routing_number": "110000000"
                    }
                },
                "linked_flows": {
                    "credit_reversal": null,
                    "issuing_},
                    "livemode": false,
                    "network": "ach",
                    "reversal_details": {
                        "deadline": 1681084800,
                        "restricted_reason": null
                    },
                    "status": "succeeded",
                    "transaction": "trxn_1MtkSr2eZvKYlo2CuFFh9Rh0"
                }
                {
                    "id": "rc_1MtkSr2eZvKYlo2CcysvUbEw",
                    "object": "treasury.received_credit",
                    "amount": 1000,
                    "created": 1680755425,
                    "currency": "usd",
                    "description": "Stripe Test",
                    "failure_code": null,
                    "financial_account": "fa_1MtkSr2eZvKYlo2CsJozwFWD",
                    "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOKVuaEGMgagXvSInCY6NpMvimqdsEKNHRrHZ3OGyVm_l5LfDMezNeY83F5Mq-rryXZ-J1z-jfFBv30wz5WxDH97VRBIzw",
                    "initiating_payment_method_details": {
                        "billing_details": {
                            "address": {
                                "city": null,
                                "country": null,
                                "line1": null,
                                "line2": null,
                                "postal_code": null,
                                "state": null
                            },
                            "email": null,
                            "name": "Jane Austen"
                        },
                        "type": "us_bank_account",
                        "us_bank_account": {
                            "bank_name": "STRIPE TEST BANK",
                            "last4": "6789",
                            "routing_number": "110000000"
                        }
                    },
                    "linked_flows": {
                        "credit_reversal": null,
                        "issuing_
                            stripe treasury received_credits list \
                                                             - -financial - account = fa_1MtkSr2eZvKYlo2CsJozwFWD \
                                                                                      - -limit = 3
{
    "object": "list",
    "url": "/v1/treasury/received_credits",
    "has_more": false,
    "data": [
        {
            "id": "rc_1MtkSr2eZvKYlo2CcysvUbEw",
            "object": "treasury.received_credit",
            "amount": 1000,
            "created": 1680755425,
            "currency": "usd",
            "description": "Stripe Test",
            "failure_code": null,
            "financial_account": "fa_1MtkSr2eZvKYlo2CsJozwFWD",
            "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOKVuaEGMgagXvSInCY6NpMvimqdsEKNHRrHZ3OGyVm_l5LfDMezNeY83F5Mq-rryXZ-J1z-jfFBv30wz5WxDH97VRBIzw",
            "initiating_payment_method_details": {
                "billing_details": {
                    "address": {
                        "city": null,
                        "country": null,
                        "line1": null,
                        "line2": null,
                        "postal_code": null,
                        "state": null
                    },
                    "email": null,
                    "name": "Jane Austen"
                },
                "type": "us_bank_account",
                {
                    "id": "rd_1MtkUY2eZvKYlo2CT9SYD1AF",
                    "object": "treasury.received_debit",
                    "amount": 1000,
                    "created": 1680755530,
                    "currency": "usd",
                    "description": "Stripe Test",
                    "failure_code": null,
                    "financial_account": "fa_1MtkUY2eZvKYlo2CY3s6OQyK",
                    "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKMqWuaEGMgaYNwvP2Oc6NpPGJjaET9tspjuPmbhoXvIfQj6YrtJkjCiTFYe59B8Ck4cg5jTS80A9mLSaK_4oF_LBDlNzgg",
                    "initiating_payment_method_details": {
                        "billing_details": {
                            "address": {
                                "city": null,
                                "country": null,
                                "line1": null,
                                "line2": null,
                                "postal_code": null,
                                "state": null
                            },
                            "email": null,
                            "name": "Jane Austen"
                        },
                        "type": "us_bank_account",
                        "us_bank_account": {
                            "bank_name": "STRIPE TEST BANK",
                            "last4": "6789",
                            "routing_number": "110000000"
                        }
                    },
                    "linked_flows": {
                        "debit_reversal": null,
                        "inbound_tr
                            stripe treasury received_debits retrieve rd_1MtkUY2eZvKYlo2CT9SYD1AF


                        {
                            "id": "rd_1MtkUY2eZvKYlo2CT9SYD1AF",
                            "object": "treasury.received_debit",
                            "amount": 1000,
                            "created": 1680755530,
                            "currency": "usd",
                            "description": "Stripe Test",
                            "failure_code": null,
                            "financial_account": "fa_1MtkUY2eZvKYlo2CY3s6OQyK",
                            "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKMqWuaEGMgaYNwvP2Oc6NpPGJjaET9tspjuPmbhoXvIfQj6YrtJkjCiTFYe59B8Ck4cg5jTS80A9mLSaK_4oF_LBDlNzgg",
                            "initiating_payment_method_details": {
                                "billing_details": {
                                    "address": {
                                        "city": null,
                                        "country": null,
                                        "line1": null,
                                        "line2": null,
                                        "postal_code": null,
                                        "state": null
                                    },
                                    "email": null,
                                    "name": "Jane Austen"
                                },
                                "type": "us_bank_account",
                                "us_bank_account": {
                                    "bank_name": "STRIPE TEST BANK",
                                    "last4": "6789",
                                    "routing_number": "110000000"
                                }
                            },
                            "linked_flows": {
                                "debit_reversal": null,
                                "inbound_
                                    stripe treasury received_debits list \
                                                                    - -financial - account = fa_1MtkUY2eZvKYlo2CY3s6OQyK \
                                                                                             - -limit = 3
{
    "object": "list",
    "url": "/v1/treasury/received_debits",
    "has_more": false,
    "data": [
        {
            "id": "rd_1MtkUY2eZvKYlo2CT9SYD1AF",
            "object": "treasury.received_debit",
            "amount": 1000,
            "created": 1680755530,
            "currency": "usd",
            "description": "Stripe Test",
            "failure_code": null,
            "financial_account": "fa_1MtkUY2eZvKYlo2CY3s6OQyK",
            "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKMqWuaEGMgaYNwvP2Oc6NpPGJjaET9tspjuPmbhoXvIfQj6YrtJkjCiTFYe59B8Ck4cg5jTS80A9mLSaK_4oF_LBDlNzgg",
            "initiating_payment_method_details": {
                "billing_details": {
                    "address": {
                        "city": null,
                        "country": null,
                        "line1": null,
                        "line2": null,
                        "postal_code": null,
                        "state": null
                    },
                    "email": null,
                    "name": "Jane Austen"
                },
                "type": "us_bank_account",
                l,
            "issuing_authorization": null,
            "issuing_transaction": null,
            "payout": null
        },
        "livemode": false,
"network": "ach",
"reversal_details": {
    "deadline": 1681084800,
    "restricted_reason": null
},
"status": "succeeded",
"transaction": "trxn_1MtkUY2eZvKYlo2ChymLKPp5"
}
{...}
{...}
],
}
stripe
test_helpers
treasury
received_debits
create \
- -amount = 1000 \
            - -currency = usd \
                          - -financial - account = fa_1MtkUY2eZvKYlo2CY3s6OQyK \
                                                   - -network = ach
{
    "id": "rd_1MtkUY2eZvKYlo2CT9SYD1AF",
    "object": "treasury.received_debit",
    "amount": 1000,
    "created": 1680755530,
    "currency": "usd",
    "description": "Stripe Test",
    "failure_code": null,
    "financial_account": "fa_1MtkUY2eZvKYlo2CY3s6OQyK",
    "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKMqWuaEGMgaYNwvP2Oc6NpPGJjaET9tspjuPmbhoXvIfQj6YrtJkjCiTFYe59B8Ck4cg5jTS80A9mLSaK_4oF_LBDlNzgg",
    "initiating_payment_method_details": {
        "billing_details": {
            "address": {
                "city": null,
                "country": null,
                "line1": null,
                "line2": null,
                "postal_code": null,
                "state": null
            },
            "email": null,
            "name": "Jane Austen"
        },
        "type": "us_bank_account",
        "us_bank_account": {
            "bank_name": "STRIPE TEST BANK",
            "last4": "6789",
            "routing_number": "110000000"
        }
    },
    "linked_flows": {
        "debit_reversal": null,
        "inbound_tr
            {
                "id": "credrev_1Mtklw2eZvKYlo2CJG2MWJM7",
                "object": "treasury.credit_reversal",
                "amount": 1000,
                "created": 1680756608,
                "currency": "usd",
                "financial_account": "fa_1Mtklw2eZvKYlo2CNHscZzs2",
                "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKICfuaEGMgYv0T_PcXU6NpP_n6wAfI9LKta3LkDRNQT8oLGdQf7JcXsskGjrq1LICpYVy5a3oOBI5gaVvTy8MtwpT1PTpQ",
                "livemode": false,
                "metadata": {},
                "network": "ach",
                "received_credit": "rc_1Mtklw2eZvKYlo2CxuluQFPR",
                "status": "processing",
                "status_transitions": {
                    "posted_at": null
                },
                "transaction": "trxn_1Mtklw2eZvKYlo2CKkbNA2TS"
            }
        stripe treasury credit_reversals create \
                                         - -received - credit = rc_1MtkGJLkdIwHu7ixWPuY9DGn
{
    "id": "credrev_1Mtklw2eZvKYlo2CJG2MWJM7",
    "object": "treasury.credit_reversal",
    "amount": 1000,
    "created": 1680756608,
    "currency": "usd",
    "financial_account": "fa_1Mtklw2eZvKYlo2CNHscZzs2",
    "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKICfuaEGMgYv0T_PcXU6NpP_n6wAfI9LKta3LkDRNQT8oLGdQf7JcXsskGjrq1LICpYVy5a3oOBI5gaVvTy8MtwpT1PTpQ",
    "livemode": false,
    "metadata": {},
    "network": "ach",
    "received_credit": "rc_1Mtklw2eZvKYlo2CxuluQFPR",
    "status": "processing",
    "status_transitions": {
        "posted_at": null
    },
    "transaction": "trxn_1Mtklw2eZvKYlo2CKkbNA2TS"
}
{
    "id": "credrev_1Mtklw2eZvKYlo2CJG2MWJM7",
    "object": "treasury.credit_reversal",
    "amount": 1000,
    "created": 1680756608,
    "currency": "usd",
    "financial_account": "fa_1Mtklw2eZvKYlo2CNHscZzs2",
    "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKICfuaEGMgYv0T_PcXU6NpP_n6wAfI9LKta3LkDRNQT8oLGdQf7JcXsskGjrq1LICpYVy5a3oOBI5gaVvTy8MtwpT1PTpQ",
    "livemode": false,
    "metadata": {},
    "network": "ach",
    "received_credit": "rc_1Mtklw2eZvKYlo2CxuluQFPR",
    "status": "processing",
    "status_transitions": {
        "posted_at": null
    },
    "transaction": "trxn_1Mtklw2eZvKYlo2CKkbNA2TS"
}
{
    "id": "credrev_1Mtklw2eZvKYlo2CJG2MWJM7",
    "object": "treasury.credit_reversal",
    "amount": 1000,
    "created": 1680756608,
    "currency": "usd",
    "financial_account": "fa_1Mtklw2eZvKYlo2CNHscZzs2",
    "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKICfuaEGMgYv0T_PcXU6NpP_n6wAfI9LKta3LkDRNQT8oLGdQf7JcXsskGjrq1LICpYVy5a3oOBI5gaVvTy8MtwpT1PTpQ",
    "livemode": false,
    "metadata": {},
    "network": "ach",
    "received_credit": "rc_1Mtklw2eZvKYlo2CxuluQFPR",
    "status": "processing",
    "status_transitions": {
        "posted_at": null
    },
    "transaction": "trxn_1Mtklw2eZvKYlo2CKkbNA2TS"
}
stripe
treasury
credit_reversals
list \
- -financial - account = fa_1MtkGJLkdIwHu7ix6FAcfxof \
                         - -limit = 3
{
    "object": "list",
    "url": "/v1/treasury/credit_reversals",
    "has_more": false,
    "data": [
        {
            "id": "credrev_1Mtklw2eZvKYlo2CJG2MWJM7",
            "object": "treasury.credit_reversal",
            "amount": 1000,
            "created": 1680756608,
            "currency": "usd",
            "financial_account": "fa_1Mtklw2eZvKYlo2CNHscZzs2",
            "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKICfuaEGMgYv0T_PcXU6NpP_n6wAfI9LKta3LkDRNQT8oLGdQf7JcXsskGjrq1LICpYVy5a3oOBI5gaVvTy8MtwpT1PTpQ",
            "livemode": false,
            "metadata": {},
            "network": "ach",
            "received_credit": "rc_1Mtklw2eZvKYlo2CxuluQFPR",
            "status": "processing",
            "status_transitions": {
                "posted_at": null
            },
            "transaction": "trxn_1Mtklw2eZvKYlo2CKkbNA2TS"
        }
        {...}
        {...}
    ],
}
{
    "id": "debrev_1MtkMLLkdIwHu7ixIcVctOKK",
    "object": "treasury.debit_reversal",
    "amount": 1000,
    "created": 1680755021,
    "currency": "usd",
    "financial_account": "fa_1MtkMLLkdIwHu7ixrkGP4bqB",
    "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KM6SuaEGMgaqNYp8YbE6NpNWYhI1PSbr_jlZwdPHUJHYBRG6-5T1Bmpq4GkpUhVvzLMDWZWkMVIveXHgiVwLUgpMM4Jx8w",
    "linked_flows": null,
    "livemode": false,
    "metadata": {},
    "network": "ach",
    "received_debit": "rd_1MtkMLLkdIwHu7ixoiUFN4qd",
    "status": "processing",
    "status_transitions": {
        "completed_at": null
    },
    "transaction": "trxn_1MtkMLLkdIwHu7ix2BG3LwWW"
}
stripe
treasury
debit_reversals
create \
- -received - debit = rd_1MtkMLLkdIwHu7ixoiUFN4qd
{
    "id": "debrev_1MtkMLLkdIwHu7ixIcVctOKK",
    "object": "treasury.debit_reversal",
    "amount": 1000,
    "created": 1680755021,
    "currency": "usd",
    "financial_account": "fa_1MtkMLLkdIwHu7ixrkGP4bqB",
    "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KM6SuaEGMgaqNYp8YbE6NpNWYhI1PSbr_jlZwdPHUJHYBRG6-5T1Bmpq4GkpUhVvzLMDWZWkMVIveXHgiVwLUgpMM4Jx8w",
    "linked_flows": null,
    "livemode": false,
    "metadata": {},
    "network": "ach",
    "received_debit": "rd_1MtkMLLkdIwHu7ixoiUFN4qd",
    "status": "processing",
    "status_transitions": {
        "completed_at": null
    },
    "transaction": "trxn_1MtkMLLkdIwHu7ix2BG3LwWW"
}
stripe
treasury
debit_reversals
retrieve
debrev_1MtkMLLkdIwHu7ixIcVctOKK
{
    "id": "debrev_1MtkMLLkdIwHu7ixIcVctOKK",
    "object": "treasury.debit_reversal",
    "amount": 1000,
    "created": 1680755021,
    "currency": "usd",
    "financial_account": "fa_1MtkMLLkdIwHu7ixrkGP4bqB",
    "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KM6SuaEGMgaqNYp8YbE6NpNWYhI1PSbr_jlZwdPHUJHYBRG6-5T1Bmpq4GkpUhVvzLMDWZWkMVIveXHgiVwLUgpMM4Jx8w",
    "linked_flows": null,
    "livemode": false,
    "metadata": {},
    "network": "ach",
    "received_debit": "rd_1MtkMLLkdIwHu7ixoiUFN4qd",
    "status": "processing",
    "status_transitions": {
        "completed_at": null
    },
    "transaction": "trxn_1MtkMLLkdIwHu7ix2BG3LwWW"
}
stripe
treasury
debit_reversals
list \
- -financial - account = fa_1MtkMLLkdIwHu7ixrkGP4bqB \
                         - -limit = 3
stripe
treasury
debit_reversals
list \
- -financial - account = fa_1MtkMLLkdIwHu7ixrkGP4bqB \
                         - -limit = 3
{
    "object": "list",
    "url": "/v1/treasury/debit_reversals",
    "has_more": false,
    "data": [
        {
            "id": "debrev_1MtkMLLkdIwHu7ixIcVctOKK",
            "object": "treasury.debit_reversal",
            "amount": 1000,
            "created": 1680755021,
            "currency": "usd",
            "financial_account": "fa_1MtkMLLkdIwHu7ixrkGP4bqB",
            "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KM6SuaEGMgaqNYp8YbE6NpNWYhI1PSbr_jlZwdPHUJHYBRG6-5T1Bmpq4GkpUhVvzLMDWZWkMVIveXHgiVwLUgpMM4Jx8w",
            "linked_flows": null,
            "livemode": false,
            "metadata": {},
            "network": "ach",
            "received_debit": "rd_1MtkMLLkdIwHu7ixoiUFN4qd",
            "status": "processing",
            "status_transitions": {
                "completed_at": null
            },
            "transaction": "trxn_1MtkMLLkdIwHu7ix2BG3LwWW"
        }
        {...}
        {...}
    ],
}
{
    "id": "ent_test_61QG5x2cU1GluFTYs41JqiESbLiX8C8O",
    "object": "entitlements.active_entitlement",
    "feature": "feat_test_61QGU1MWyFMSP9YBZ41ClCIKljWvsTgu",
    "lookup_key": "seats-feature",
    "livemode": false
}
stripe
entitlements
active_entitlements
retrieve
ent_test_61QG5x2cU1GluFTYs41JqiESbLiX8C8O
{
    "id": "ent_test_61QG5x2cU1GluFTYs41JqiESbLiX8C8O",
    "object": "entitlements.active_entitlement",
    "feature": "feat_test_61QGU1MWyFMSP9YBZ41ClCIKljWvsTgu",
    "lookup_key": "seats-feature",
    "livemode": false
}
stripe
entitlements
active_entitlements
list \
- -customer = cus_9s6XKzkNRiz8i3
{
    "object": "list",
    "url": "/v1/entitlements/active_entitlements",
    "has_more": false,
    "data": [
        {
            "id": "ent_test_61QG5x2cU1GluFTYs41JqiESbLiX8C8O",
            "object": "entitlements.active_entitlement",
            "feature": "feat_test_61QGU1MWyFMSP9YBZ41ClCIKljWvsTgu",
            "lookup_key": "seats-feature",
            "livemode": false
        }
        {...}
        {...}
    ],
}
{
    "id": "frr_1MrQwrLkdIwHu7ixUov4x2b3",
    "object": "reporting.report_run",
    "created": 1680203749,
    "error": null,
    "livemode": false,
    "parameters": {
        "interval_end": 1680100000,
        "interval_start": 1680000000
    },
    "report_type": "balance.summary.1",
    "result": null,
    "status": "pending",
    "succeeded_at": null
}
stripe
reporting
report_runs
create \
- -report - type = "balance.summary.1" \
                   - d
"parameters[interval_start]" = 1680000000 \
                               - d
"parameters[interval_end]" = 1680100000
{
    "id": "frr_1MrQwrLkdIwHu7ixUov4x2b3",
    "object": "reporting.report_run",
    "created": 1680203749,
    "error": null,
    "livemode": false,
    "parameters": {
        "interval_end": 1680100000,
        "interval_start": 1680000000
    },
    "report_type": "balance.summary.1",
    "result": null,
    "status": "pending",
    "succeeded_at": null
}
stripe
reporting
report_runs
retrieve
frr_1MrQwrLkdIwHu7ixUov4x2b3
{
    "id": "frr_1MrQwrLkdIwHu7ixUov4x2b3",
    "object": "reporting.report_run",
    "created": 1680203749,
    "error": null,
    "livemode": false,
    "parameters": {
        "interval_end": 1680100000,
        "interval_start": 1680000000
    },
    "report_type": "balance.summary.1",
    "result": null,
    "status": "pending",
    "succeeded_at": null
}
stripe
reporting
report_runs
list \
- -limit = 3
{
    "object": "list",
    "url": "/v1/reporting/report_runs",
    "has_more": false,
    "data": [
        {
            "id": "frr_1MrQwrLkdIwHu7ixUov4x2b3",
            "object": "reporting.report_run",
            "created": 1680203749,
            "error": null,
            "livemode": false,
            "parameters": {
                "interval_end": 1680100000,
                "interval_start": 1680000000
            },
            "report_type": "balance.summary.1",
            "result": null,
            "status": "pending",
            "succeeded_at": null
        }
        {...}
        {...}
    ],
}
{
    "id": "fca_1MwVK82eZvKYlo2Cjw8FMxXf",
    "object": "linked_account",
    "account_holder": {
        "customer": "cus_9s6XI9OFIdpjIg",
        "type": "customer"
    },
    "balance": null,
    "balance_refresh": null,
    "category": "cash",
    "created": 1681412208,
    "display_name": "Sample Checking Account",
    "institution_name": "StripeBank",
    "last4": "6789",
    "livemode": false,
    "ownership": null,
    "ownership_refresh": null,
    "permissions": [],
    "status": "active",
    "subcategory": "checking",
    "subscriptions": [],
    "supported_payment_method_types": [
        "us_bank_account"
    ],
    "transaction_refresh": null
}
stripe
financial_connections
accounts
retrieve
fca_1MwVK82eZvKYlo2Cjw8FMxXf
{
    "id": "fca_1MwVK82eZvKYlo2Cjw8FMxXf",
    "object": "linked_account",
    "account_holder": {
        "customer": "cus_9s6XI9OFIdpjIg",
        "type": "customer"
    },
    "balance": null,
    "balance_refresh": null,
    "category": "cash",
    "created": 1681412208,
    "display_name": "Sample Checking Account",
    "institution_name": "StripeBank",
    "last4": "6789",
    "livemode": false,
    "ownership": null,
    "ownership_refresh": null,
    "permissions": [],
    "status": "active",
    "subcategory": "checking",
    "subscriptions": [],
    "supported_payment_method_types": [
        "us_bank_account"
    ],
    "transaction_refresh": null
}
stripe
financial_connections
accounts
list \
- -limit = 3
{
    "object": "list",
    "url": "/v1/financial_connections/accounts",
    "has_more": false,
    "data": [
        {
            "id": "fca_1MwVK82eZvKYlo2Cjw8FMxXf",
            "object": "linked_account",
            "account_holder": {
                "customer": "cus_9s6XI9OFIdpjIg",
                "type": "customer"
            },
            "balance": null,
            "balance_refresh": null,
            "category": "cash",
            "created": 1681412208,
            "display_name": "Sample Checking Account",
            "institution_name": "StripeBank",
            "last4": "6789",
            "livemode": false,
            "ownership": null,
            "ownership_refresh": null,
            "permissions": [],
            "status": "active",
            "subcategory": "checking",
            "subscriptions": [],
            "supported_payment_method_types": [
                "us_bank_account"
            ],
            "transaction_refresh": null
        }
        {...}
        {...}
    ],
}
stripe
financial_connections
accounts
disconnect
fca_1MwVK82eZvKYlo2Cjw8FMxXf
{
    "id": "fca_1MwVK82eZvKYlo2Cjw8FMxXf",
    "object": "linked_account",
    "account_holder": {
        "customer": "cus_9s6XI9OFIdpjIg",
        "type": "customer"
    },
    "balance": null,
    "balance_refresh": null,
    "category": "cash",
    "created": 1681412208,
    "display_name": "Sample Checking Account",
    "institution_name": "StripeBank",
    "last4": "6789",
    "livemode": false,
    "ownership": null,
    "ownership_refresh": null,
    "permissions": [],
    "status": "disconnected",
    "subcategory": "checking",
    "subscriptions": [],
    "supported_payment_method_types": [
        "us_bank_account"
    ],
    "transaction_refresh": null
}
stripe
financial_connections
accounts
refresh
fca_1MwVK82eZvKYlo2Cjw8FMxXf \
- d
"features[0]" = balance
{
    "id": "fca_1MwVK82eZvKYlo2Cjw8FMxXf",
    "object": "linked_account",
    "account_holder": {
        "customer": "cus_9s6XI9OFIdpjIg",
        "type": "customer"
    },
    "balance": null,
    "balance_refresh": {
        "status": "pending",
        "last_attempted_at": 1681422295
    },
    "category": "cash",
    "created": 1681412208,
    "display_name": "Sample Checking Account",
    "institution_name": "StripeBank",
    "last4": "6789",
    "livemode": false,
    "ownership": null,
    "ownership_refresh": null,
    "permissions": [],
    "status": "pending",
    "subcategory": "checking",
    "subscriptions": [],
    "supported_payment_method_types": [
        "us_bank_account"
    ],
    "transaction_refresh": null
}
stripe
financial_connections
accounts
subscribe
fca_1NQay62eZvKYlo2C8dflHjWB \
- d
"features[0]" = transactions
{
    "id": "fca_1NQay62eZvKYlo2C8dflHjWB",
    "object": "linked_account",
    "account_holder": {
        "customer": "cus_9s6XKzkNRiz8i3",
        "type": "customer"
    },
    "balance": null,
    "balance_refresh": null,
    "category": "cash",
    "created": 1688583746,
    "display_name": "Sample Checking Account",
    "institution_name": "StripeBank",
    "last4": "6789",
    "livemode": false,
    "ownership": null,
    "ownership_refresh": null,
    "permissions": [],
    "status": "active",
    "subcategory": "checking",
    "subscriptions": [
        "transactions"
    ],
    "supported_payment_method_types": [
        "us_bank_account"
    ],
    "transaction_refresh": {
        "id": "fctxnref_OD10iHSd7eaheDkeabbQfnJ7",
        "status": "pending",
        "last_attempted_at": 1625337296
    }
}
stripe
financial_connections
accounts
unsubscribe
fca_1NQayH2eZvKYlo2CMBkU6Y9s \
- d
"features[0]" = transactions

{
    "id": "fca_1NQayH2eZvKYlo2CMBkU6Y9s",
    "object": "linked_account",
    "account_holder": {
        "customer": "cus_9s6XKzkNRiz8i3",
        "type": "customer"
    },
    "balance": null,
    "balance_refresh": null,
    "category": "cash",
    "created": 1688583757,
    "display_name": "Sample Checking Account",
    "institution_name": "StripeBank",
    "last4": "6789",
    "livemode": false,
    "ownership": null,
    "ownership_refresh": null,
    "permissions": [],
    "status": "active",
    "subcategory": "checking",
    "subscriptions": [],
    "supported_payment_method_types": [
        "us_bank_account"
    ],
    "transaction_refresh": {
        "id": "fctxnref_OD10EqMBikeOrWm7JW44fdpo",
        "status": "succeeded",
        "last_attempted_at": 1625337296
    }
}
{
    "id": "fcaown_1NtI9uBHO5VeT9SUKLJU5suZ",
    "object": "financial_connections.account_owner",
    "email": "nobody+janesmith@stripe.com",
    "name": "Jane Smith",
    "ownership": "fcaowns_1NtI9uBHO5VeT9SUSRe21lqt",
    "phone": "+1 555-555-5555",
    "raw_address": "123 Main Street, Everytown USA",
    "refreshed_at": null
}
{
    "id": "fcaowns_1MwVKR2eZvKYlo2CGV7Mmt6s",
    "object": "linked_account_ownership",
    "created": 1681412227,
    "owners": {
        "object": "list",
        "data": [],
        "has_more": false,
        "url": "/v1/linked_accounts/fca_1MwVKR2eZvKYlo2CoMV2L3PV/owners?ownership=fcaowns_1MwVKR2eZvKYlo2CGV7Mmt6s"
    }
}
stripe
financial_connections
accounts
list_owners
fca_1NoEbE2eZvKYlo2CmmnAn2A1 \
- -ownership = fcaowns_1NoEbE2eZvKYlo2C4Xj7vilA
{
    "object": "list",
    "url": "/v1/financial_connections/accounts/fca_1NoEbE2eZvKYlo2CmmnAn2A1/owners",
    "has_more": false,
    "data": [
        {
            "object": "list",
            "url": "/v1/financial_connections/accounts/fca_1NoDzC2eZvKYlo2CwXpqO27d/owners",
            "has_more": false,
            "data": [
                {
                    "id": "fcaown_1NoDzC2eZvKYlo2C1TlEZ0K2",
                    "object": "linked_account_owner",
                    "email": "nobody+janesmith@stripe.com",
                    "name": "Jane Smith",
                    "ownership": "fcaowns_1NoDzC2eZvKYlo2CAm1EDKTk",
                    "phone": "+1 555-555-5555",
                    "raw_address": "123 Main Street, Everytown USA",
                    "refreshed_at": null
                }
            ]
        }
        {...}
        {...}
    ],
}
{
    "id": "fcsess_1MwtnGLkdIwHu7ixs7NPQ7dq",
    "object": "financial_connections.session",
    "account_holder": {
        "customer": "cus_NiKSWdaFz2F6I0",
        "type": "customer"
    },
    "accounts": {
        "object": "list",
        "data": [],
        "has_more": false,
        "total_count": 0,
        "url": "/v1/financial_connections/accounts"
    },
    "client_secret": "fcsess_client_secret_KRJTKvCY3IKoYTrW18EazcO3",
    "filters": {
        "countries": [
            "US"
        ]
    },
    "livemode": false,
    "permissions": [
        "balances",
        "payment_method"
    ]
}
stripe
financial_connections
sessions
create \
- d
"account_holder[type]" = customer \
                         - d
"account_holder[customer]" = cus_NiKSWdaFz2F6I0 \
                             - d
"permissions[0]" = payment_method \
                   - d
"permissions[1]" = balances \
                   - d
"filters[countries][0]" = US
{
    "id": "fcsess_1MwtnGLkdIwHu7ixs7NPQ7dq",
    "object": "financial_connections.session",
    "account_holder": {
        "customer": "cus_NiKSWdaFz2F6I0",
        "type": "customer"
    },
    "accounts": {
        "object": "list",
        "data": [],
        "has_more": false,
        "total_count": 0,
        "url": "/v1/financial_connections/accounts"
    },
    "client_secret": "fcsess_client_secret_KRJTKvCY3IKoYTrW18EazcO3",
    "filters": {
        "countries": [
            "US"
        ]
    },
    "livemode": false,
    "permissions": [
        "balances",
        "payment_method"
    ]
}
stripe
financial_connections
sessions
retrieve
fcsess_1MwtnGLkdIwHu7ixs7NPQ7dq
stripe
financial_connections
sessions
retrieve
fcsess_1MwtnGLkdIwHu7ixs7NPQ7dq
{
    "id": "fcsess_1MwtnGLkdIwHu7ixs7NPQ7dq",
    "object": "financial_connections.session",
    "account_holder": {
        "customer": "cus_NiKSWdaFz2F6I0",
        "type": "customer"
    },
    "accounts": {
        "object": "list",
        "data": [],
        "has_more": false,
        "total_count": 0,
        "url": "/v1/financial_connections/accounts"
    },
    "client_secret": "fcsess_client_secret_KRJTKvCY3IKoYTrW18EazcO3",
    "filters": {
        "countries": [
            "US"
        ]
    },
    "livemode": false,
    "permissions": [
        "balances",
        "payment_method"
    ]
}
{
    "id": "fctxn_1MwVKd2eZvKYlo2ChNw2UxSa",
    "object": "financial_connections.transaction",
    "account": "fca_1MwVKd2eZvKYlo2CnlgoF3I4",
    "amount": 300,
    "currency": "usd",
    "description": "Rocket Rides",
    "livemode": false,
    "status": "posted",
    "status_transitions": {
        "posted_at": 1681412239,
        "void_at": null
    },
    "transacted_at": 1681412239,
    "transaction_refresh": "fctxnref_NhvAgiKSFDg9jOe6eIlj41X5",
    "updated": 1681412239
}
stripe
financial_connections
transactions
retrieve
fctxn_1MwVKd2eZvKYlo2ChNw2UxSa
{
    "id": "fctxn_1MwVKd2eZvKYlo2ChNw2UxSa",
    "object": "financial_connections.transaction",
    "account": "fca_1MwVKd2eZvKYlo2CnlgoF3I4",
    "amount": 300,
    "currency": "usd",
    "description": "Rocket Rides",
    "livemode": false,
    "status": "posted",
    "status_transitions": {
        "posted_at": 1681412239,
        "void_at": null
    },
    "transacted_at": 1681412239,
    "transaction_refresh": "fctxnref_NhvAgiKSFDg9jOe6eIlj41X5",
    "updated": 1681412239
}
stripe
financial_connections
transactions
list \
- -account = fca_1NpHiT2eZvKYlo2C6pRwOFjr \
             - -limit = 3
{
    "object": "list",
    "url": "/v1/financial_connections/transactions",
    "has_more": false,
    "data": [
        {
            "id": "fctxn_1NpHiT2eZvKYlo2CZFvnM3HJ",
            "object": "financial_connections.transaction",
            "account": "fca_1NpHiT2eZvKYlo2C6pRwOFjr",
            "amount": 300,
            "currency": "usd",
            "description": "Rocket Rides",
            "livemode": false,
            "status": "posted",
            "status_transitions": {
                "posted_at": 1694467941,
                "void_at": null
            },
            "transacted_at": 1694467941,
            "transaction_refresh": "fctxnref_OcWmGrWptAdJ2bmpYE2P0Hws",
            "updated": 1694467941
        }
        {...}
        {...}
    ],
}

{
    "id": "taxcalc_1OduxkBUZ691iUZ4iWvpMApI",
    "object": "tax.calculation",
    "amount_total": 1953,
    "currency": "usd",
    "customer": null,
    "customer_details": {
        "address": {
            "city": "Seattle",
            "country": "US",
            "line1": "920 5th Ave",
            "line2": null,
            "postal_code": "98104",
            "state": "WA"
        },
        "address_source": "shipping",
        "ip_address": null,
        "tax_ids": [],
        "taxability_override": "none"
    },
    "expires_at": 1706708005,
    "line_items": {
        "object": "list",
        "data": [
            {
                "id": "tax_li_PSqf3RMNZa23H4",
                "object": "tax.calculation_line_item",
                "amount": 1499,
                "amount_tax": 154,
                "livemode": false,
                "product": null,
                "quantity": 1,
                "reference": "Music Streaming Coupon",
                "tax_behavior": "exclusive",
                "tax_code": "txcd_10000000"
            }
        ],
        "has_more": false,
        "total_count": 1,
        "url": "/v1/tax/calculations/taxcalc_1Odux
        stripe tax calculations create \
                                - -currency = usd \
                                              - d
"customer_details[address][line1]" = "920 5th Ave" \
                                     - d
"customer_details[address][city]" = Seattle \
                                    - d
"customer_details[address][state]" = WA \
                                     - d
"customer_details[address][postal_code]" = 98104 \
                                           - d
"customer_details[address][country]" = US \
                                       - d
"customer_details[address_source]" = shipping \
                                     - d
"line_items[0][amount]" = 1499 \
                          - d
"line_items[0][tax_code]" = txcd_10000000 \
                            - d
"line_items[0][reference]" = "Music Streaming Coupon" \
                             - d
"shipping_cost[amount]" = 300 \
                          - d
"expand[0]" = line_items
{
    "id": "taxcalc_1OduxkBUZ691iUZ4iWvpMApI",
    "object": "tax.calculation",
    "amount_total": 1953,
    "currency": "usd",
    "customer": null,
    "customer_details": {
        "address": {
            "city": "Seattle",
            "country": "US",
            "line1": "920 5th Ave",
            "line2": null,
            "postal_code": "98104",
            "state": "WA"
        },
        "address_source": "shipping",
        "ip_address": null,
        "tax_ids": [],
        "taxability_override": "none"
    },
    "expires_at": 1706708005,
    "line_items": {
        "object": "list",
        "data": [
            {
                "id": "tax_li_PSqf3RMNZa23H4",
                "object": "tax.calculation_line_item",
                "amount": 1499,
                "amount_tax": 154,
                "livemode": false,
                "product": null,
                "quantity": 1,
                "reference": "Music Streaming Coupon",
                "tax_behavior": "exclusive",
                "tax_code": "txcd_10000000"
            }
        ],
        "has_more": false,
        "total_count": 1,
        "url": "/v1/tax/calculations/taxcalc_1OduxkBclusive": false,
"tax_rate_details": {
    "country": "DE",
    "percentage_decimal": "0.0",
    "state": null,
    "tax_type": "vat"
},
"taxability_reason": "zero_rated",
"taxable_amount": 300
}
],
"tax_date": 1706535204
}
stripe
tax
calculations
list_line_items
taxcalc_1NpJD42eZvKYlo2CUti522cz \
- -limit = 3
{
    "object": "list",
    "url": "/v1/tax/calculations/taxcalc_1NpJD42eZvKYlo2CUti522cz/line_items",
    "has_more": false,
    "data": [
        {
            "object": "list",
            "url": "/v1/tax/calculations/taxcalc_1NpJD42eZvKYlo2CUti522cz/line_items",
            "has_more": false,
            "data": [
                {
                    "id": "tax_li_OcYJb5mQOSSSWD",
                    "object": "tax.calculation_line_item",
                    "amount": 1499,
                    "amount_tax": 148,
                    "livemode": false,
                    "product": null,
                    "quantity": 1,
                    "reference": "Pepperoni Pizza",
                    "tax_behavior": "exclusive",
                    "tax_code": "txcd_40060003"
                }
            ]
        }
        {...}
        {...}
    ],
}
{
    "id": "taxreg_NkyGPRPytKq66j",
    "object": "tax.registration",
    "active_from": 1682036640,
    "country": "US",
    "country_options": {
        "us": {
            "state": "CA",
            "type": "state_sales_tax"
        }
    },
    "created": 1682006400,
    "expires_at": null,
    "livemode": false,
    "status": "active",
    "state": "CA",
    "type": "standard"
}
stripe
tax
registrations
create \
- -country = US \
             - d
"country_options[us][state]" = CA \
                               - d
"country_options[us][type]" = state_sales_tax \
                              - -active -
from=now
{
    "id": "taxreg_NkyGPRPytKq66j",
    "object": "tax.registration",
    "active_from": 1682036640,
    "country": "US",
    "country_options": {
        "us": {
            "state": "CA",
            "type": "state_sales_tax"
        }
    },
    "created": 1682006400,
    "expires_at": null,
    "livemode": false,
    "status": "active",
    "state": "CA",
    "type": "standard"
}
stripe
tax
registrations
update
taxreg_NkyGPRPytKq66j \
- -expires - at = now
{
    "id": "taxreg_NkyGPRPytKq66j",
    "object": "tax.registration",
    "active_from": 1683036640,
    "country": "US",
    "country_options": {
        "us": {
            "state": "CA",
            "type": "state_sales_tax"
        }
    },
    "created": 1682006400,
    "expires_at": 1684072000,
    "livemode": false,
    "status": "active",
    "state": "CA",
    "type": "standard"
}
stripe
tax
registrations
retrieve
taxreg_NkyGPRPytKq66j
{
    "id": "taxreg_NkyGPRPytKq66j",
    "object": "tax.registration",
    "active_from": 1682036640,
    "country": "US",
    "country_options": {
        "us": {
            "state": "CA",
            "type": "state_sales_tax"
        }
    },
    "created": 1682006400,
    "expires_at": null,
    "livemode": false,
    "status": "active",
    "state": "CA",
    "type": "standard"
}

{
    "id": "taxreg_NkyGPRPytKq66j",
    "object": "tax.registration",
    "active_from": 1682036640,
    "country": "US",
    "country_options": {
        "us": {
            "state": "CA",
            "type": "state_sales_tax"
        }
    },
    "created": 1682006400,
    "expires_at": null,
    "livemode": false,
    "status": "active",
    "state": "CA",
    "type": "standard"
}
stripe
tax
registrations
list \
- -limit = 3
{
    "object": "list",
    "url": "/v1/tax/registrations",
    "has_more": false,
    "data": [
        {
            "id": "taxreg_NkyGPRPytKq66j",
            "object": "tax.registration",
            "active_from": 1682036640,
            "country": "US",
            "country_options": {
                "us": {
                    "state": "CA",
                    "type": "state_sales_tax"
                }
            },
            "created": 1682006400,
            "expires_at": null,
            "livemode": false,
            "status": "active",
            "state": "CA",
            "type": "standard"
        }
        {...}
        {...}
    ],
}
{
    "id": "tax_1NaS0I2eZvKYlo2CRuMhUcmz",
    "object": "tax.transaction",
    "created": 1690932566,
    "currency": "usd",
    "customer": null,
    "customer_details": {
        "address": {
            "city": "South San Francisco",
            "country": "US",
            "line1": "354 Oyster Point Blvd",
            "line2": "",
            "postal_code": "94080",
            "state": "CA"
        },
        "address_source": "shipping",
        "ip_address": null,
        "tax_ids": [],
        "taxability_override": "none"
    },
    "line_items": {
        "object": "list",
        "data": [
            {
                "id": "tax_li_ONCP443tgfS8I1",
                "object": "tax.transaction_line_item",
                "amount": 1499,
                "amount_tax": 148,
                "livemode": false,
                "metadata": null,
                "product": null,
                "quantity": 1,
                "reference": "Pepperoni Pizza",
                "reversal": null,
                "tax_behavior": "exclusive",
                "tax_code": "txcd_40060003",
                "type": "transaction"
            }
        ],
        "has_more": false,

        stripe tax transactions create_reversal \
                                - -mode = partial \
                                          - -original - transaction = tax_1NaTVd2eZvKYlo2CoOX2Nf7P \
                                                                      - -reference = myOrder_123 - refund_1 \
                                                                                     - d
"line_items[0][amount]" = -1499 \
                          - d
"line_items[0][amount_tax]" = -148 \
                              - d
"line_items[0][original_line_item]" = tax_li_ONDxh8JZw14sP8 \
                                      - d
"line_items[0][reference]" = "refund of Pepperoni Pizza" \
                             - d
"expand[0]" = line_items
stripe
tax
transactions
create_reversal \
- -mode = partial \
          - -original - transaction = tax_1NaTVd2eZvKYlo2CoOX2Nf7P \
                                      - -reference = myOrder_123 - refund_1 \
                                                     - d
"line_items[0][amount]" = -1499 \
                          - d
"line_items[0][amount_tax]" = -148 \
                              - d
"line_items[0][original_line_item]" = tax_li_ONDxh8JZw14sP8 \
                                      - d
"line_items[0][reference]" = "refund of Pepperoni Pizza" \
                             - d
"expand[0]" = line_items
stripe
tax
transactions
create_from_calculation \
- -calculation = taxcalc_1NaTVT2eZvKYlo2CsqGeLeU2 \
                 - -reference = myOrder_123 \
                                - d
"expand[0]" = line_items
{
    "id": "tax_1NaTVd2eZvKYlo2CoOX2Nf7P",
    "object": "tax.transaction",
    "created": 1690938353,
    "currency": "usd",
    "customer": null,
    "customer_details": {
        "address": {
            "city": null,
            "country": "US",
            "line1": "354 Oyster Point Blvd",
            "line2": "",
            "postal_code": "94080",
            "state": "CA"
        },
        "address_source": "shipping",
        "ip_address": null,
        "tax_ids": [],
        "taxability_override": "none"
    },
    "line_items": {
        "object": "list",
        "data": [
            {
                "id": "tax_li_ONDxh8JZw14sP8",
                "object": "tax.transaction_line_item",
                "amount": 1499,
                "amount_tax": 148,
                "livemode": false,
                "metadata": null,
                "product": null,
                "quantity": 1,
                "reference": "Pepperoni Pizza",
                "reversal": null,
                "tax_behavior": "exclusive",
                "tax_code": "txcd_40060003",
                "type": "transaction"
            }
        ],
        "has_more": false,
        "url": "/v1/tax/tction"
    }{
    "id": "tax_1NaTVd2eZvKYlo2CoOX2Nf7P",
    "object": "tax.transaction",
    "created": 1690938353,
    "currency": "usd",
    "customer": null,
    "customer_details": {
        "address": {
            "city": null,
            "country": "US",
            "line1": "354 Oyster Point Blvd",
            "line2": "",
            "postal_code": "94080",
            "state": "CA"
        },
        "address_source": "shipping",
        "ip_address": null,
        "tax_ids": [],
        "taxability_override": "none"
    },
    "line_items": {
        "object": "list",
        "data": [
            {
                "id": "tax_li_ONDxh8JZw14sP8",
                "object": "tax.transaction_line_item",
                "amount": 1499,
                "amount_tax": 148,
                "livemode": false,
                "metadata": null,
                "product": null,
                "quantity": 1,
                "reference": "Pepperoni Pizza",
                "reversal": null,
                "tax_behavior": "exclusive",
                "tax_code": "txcd_40060003",
                "type": "transaction"
            }
        ],
        "has_more": false,
        "url": "/v1/tax/t

        {
            "id": "tax_1NaTVd2eZvKYlo2CoOX2Nf7P",
            "object": "list",
            "url": "/v1/tax/transactions/tax_1NaTVd2eZvKYlo2CoOX2Nf7P/line_items",
            "has_more": false,
            "data": [
                {
                    "id": "tax_li_ONDxh8JZw14sP8",
                    "object": "tax.transaction_line_item",
                    "amount": 1499,
                    "amount_tax": 148,
                    "livemode": false,
                    "metadata": null,
                    "product": null,
                    "quantity": 1,
                    "reference": "Pepperoni Pizza",
                    "reversal": null,
                    "tax_behavior": "exclusive",
                    "tax_code": "txcd_40060003",
                    "type": "transaction"
                }
            ]
        }
            {
                "id": "tax_1NaTVd2eZvKYlo2CoOX2Nf7P",
                "object": "list",
                "url": "/v1/tax/transactions/tax_1NaTVd2eZvKYlo2CoOX2Nf7P/line_items",
                "has_more": false,
                "data": [
                    {
                        "id": "tax_li_ONDxh8JZw14sP8",
                        "object": "tax.transaction_line_item",
                        "amount": 1499,
                        "amount_tax": 148,
                        "livemode": false,
                        "metadata": null,
                        "product": null,
                        "quantity": 1,
                        "reference": "Pepperoni Pizza",
                        "reversal": null,
                        "tax_behavior": "exclusive",
                        "tax_code": "txcd_40060003",
                        "type": "transaction"
                    }
                ]
            }
        {
            "id": "tax_1NaS0I2eZvKYlo2CRuMhUcmz",
            "object": "tax.transaction",
            "created": 1690932566,
            "currency": "usd",
            "customer": null,
            "customer_details": {
                "address": {
                    "city": "South San Francisco",
                    "country": "US",
                    "line1": "354 Oyster Point Blvd",
                    "line2": "",
                    "postal_code": "94080",
                    "state": "CA"
                },
                "address_source": "shipping",
                "ip_address": null,
                "tax_ids": [],
                "taxability_override": "none"
            },
            "line_items": {
                "object": "list",
                "data": [
                    {
                        "id": "tax_li_ONCP443tgfS8I1",
                        "object": "tax.transaction_line_item",
                        "amount": 1499,
                        "amount_tax": 148,
                        "livemode": false,
                        "metadata": null,
                        "product": null,
                        "quantity": 1,
                        "reference": "Pepperoni Pizza",
                        "reversal": null,
                        "tax_behavior": "exclusive",
                        "tax_code": "txcd_40060003",
                        "type": "transaction"
                    }
                ],
                "has_more": false,
                {
                    "id": "vs_1NuNAILkdIwHu7ixh7OtGMLw",
                    "object": "identity.verification_session",
                    "client_secret": "...",
                    "created": 1695680526,
                    "last_error": null,
                    "last_verification_report": null,
                    "livemode": false,
                    "metadata": {},
                    "options": {
                        "document": {
                            "require_matching_selfie": true
                        }
                    },
                    "redaction": null,
                    "status": "requires_input",
                    "type": "document",
                    "url": "..."
                }stripe identity verification_sessions create \
                                                       - -type = document
{
    "id": "vs_1NuN4zLkdIwHu7ixleE6HvkI",
    "object": "identity.verification_session",
    "client_secret": "...",
    "created": 1695680197,
    "last_error": null,
    "last_verification_report": null,
    "livemode": false,
    "metadata": {},
    "options": {},
    "redaction": null,
    "status": "requires_input",
    "type": "document",
    "url": "..."
}
stripe
identity
verification_sessions
update
vs_1NuN9WLkdIwHu7ix597AR9uz \
- -type = id_number
{
    "id": "vs_1NuN9WLkdIwHu7ix597AR9uz",
    "object": "identity.verification_session",
    "client_secret": "...",
    "created": 1695680478,
    "last_error": null,
    "last_verification_report": null,
    "livemode": false,
    "metadata": {},
    "options": {},
    "redaction": null,
    "status": "requires_input",
    "type": "id_number",
    "url": "..."
}
stripe
identity
verification_sessions
retrieve
vs_1NuNAILkdIwHu7ixh7OtGMLw
{
    "id": "vs_1NuNAILkdIwHu7ixh7OtGMLw",
    "object": "identity.verification_session",
    "client_secret": "...",
    "created": 1695680526,
    "last_error": null,
    "last_verification_report": null,
    "livemode": false,
    "metadata": {},
    "options": {
        "document": {
            "require_matching_selfie": true
        }
    },
    "redaction": null,
    "status": "requires_input",
    "type": "document",
    "url": "..."
}
stripe
identity
verification_sessions
list \
- -limit = 3
{
    "object": "list",
    "url": "/v1/identity/verification_sessions",
    "has_more": false,
    "data": [
        {
            "id": "vs_1NuNAILkdIwHu7ixh7OtGMLw",
            "object": "identity.verification_session",
            "client_secret": "...",
            "created": 1695680526,
            "last_error": null,
            "last_verification_report": null,
            "livemode": false,
            "metadata": {},
            "options": {
                "document": {
                    "require_matching_selfie": true
                }
            },
            "redaction": null,
            "status": "requires_input",
            "type": "document",
            "url": "..."
        }
        {...}
        {...}
    ],
}
stripe
identity
verification_sessions
cancel
vs_1NuN3kLkdIwHu7ixk5OvTq3b
{
    "id": "vs_1NuN3kLkdIwHu7ixk5OvTq3b",
    "object": "identity.verification_session",
    "client_secret": null,
    "created": 1695680120,
    "last_error": null,
    "last_verification_report": null,
    "livemode": false,
    "metadata": {},
    "options": {
        "document": {
            "require_matching_selfie": true
        }
    },
    "redaction": null,
    "status": "canceled",
    "type": "document",
    "url": null
}
stripe
identity
verification_sessions
redact
vs_1NuN3kLkdIwHu7ixk5OvTq3b
{
    "id": "vs_1NuN3kLkdIwHu7ixk5OvTq3b",
    "object": "identity.verification_session",
    "client_secret": null,
    "created": 1695680120,
    "last_error": null,
    "last_verification_report": null,
    "livemode": false,
    "metadata": {},
    "options": {
        "document": {
            "require_matching_selfie": true
        }
    },
    "redaction": {
        "status": "processing"
    },
    "status": "canceled",
    "type": "document",
    "url": null
}
{
    "id": "cos_1NamBL2eZvKYlo2CP38sZVEW",
    "object": "crypto.onramp_session",
    "client_secret": "cos_1NamBL2eZvKYlo2CP38sZVEW_secret_B5faamUkzHbcpjy6NndGq1mMZGGCo8FhK2P",
    "created": 1691010131,
    "kyc_details_provided": false,
    "livemode": true,
    "metadata": {},
    "redirect_url": null,
    "status": "initialized",
    "transaction_details": {
        "destination_amount": null,
        "destination_currencies": [
            "btc",
            "eth",
            "matic",
            "sol",
            "xlm",
            "avax",
            "usdc"
        ],
        "destination_currency": null,
        "destination_network": null,
        "destination_networks": [
            "bitcoin",
            "ethereum",
            "base",
            "polygon",
            "solana",
            "stellar",
            "avalanche"
        ],
        "fees": null,
        "lock_wallet_address": false,
        "source_amount": null,
        "source_currency": null,
        "transaction_id": null,
        "wallet_address": null,
        "wallet_addresses": null
    }
}
curl - X
POST
https: // api.stripe.com / v1 / crypto / onramp_sessions \
          - u
"sk_test_ESDdbUTrLo4e9SC7uoQqlhd2:"
{
    "id": "cos_1NamBL2eZvKYlo2CP38sZVEW",
    "object": "crypto.onramp_session",
    "client_secret": "cos_1NamBL2eZvKYlo2CP38sZVEW_secret_B5faamUkzHbcpjy6NndGq1mMZGGCo8FhK2P",
    "created": 1691010131,
    "kyc_details_provided": false,
    "livemode": true,
    "metadata": {},
    "redirect_url": null,
    "status": "initialized",
    "transaction_details": {
        "destination_amount": null,
        "destination_currencies": [
            "btc",
            "eth",
            "matic",
            "sol",
            "xlm",
            "avax",
            "usdc"
        ],
        "destination_currency": null,
        "destination_network": null,
        "destination_networks": [
            "bitcoin",
            "ethereum",
            "base",
            "polygon",
            "solana",
            "stellar",
            "avalanche"
        ],
        "fees": null,
        "lock_wallet_address": false,
        "source_amount": null,
        "source_currency": null,
        "transaction_id": null,
        "wallet_address": null,
        "wallet_addresses": null
    }
}
curl
https: // api.stripe.com / v1 / crypto / onramp_sessions / cos_1NamBL2eZvKYlo2CP38sZVEW \
          - u
"sk_test_ESDdbUTrLo4e9SC7uoQqlhd2:"
{
    "id": "cos_1NamBL2eZvKYlo2CP38sZVEW",
    "object": "crypto.onramp_session",
    "client_secret": "cos_1NamBL2eZvKYlo2CP38sZVEW_secret_B5faamUkzHbcpjy6NndGq1mMZGGCo8FhK2P",
    "created": 1691010131,
    "kyc_details_provided": false,
    "livemode": true,
    "metadata": {},
    "redirect_url": null,
    "status": "initialized",
    "transaction_details": {
        "destination_amount": null,
        "destination_currencies": [
            "btc",
            "eth",
            "matic",
            "sol",
            "xlm",
            "avax",
            "usdc"
        ],
        "destination_currency": null,
        "destination_network": null,
        "destination_networks": [
            "bitcoin",
            "ethereum",
            "base",
            "polygon",
            "solana",
            "stellar",
            "avalanche"
        ],
        "fees": null,
        "lock_wallet_address": false,
        "source_amount": null,
        "source_currency": null,
        "transaction_id": null,
        "wallet_address": null,
        "wallet_addresses": null
    }
}

curl - G
https: // api.stripe.com / v1 / crypto / onramp_sessions \
          - u
"sk_test_ESDdbUTrLo4e9SC7uoQqlhd2:" \
- d
limit = 3
{
    "object": "list",
    "url": "/v1/crypto/onramp_sessions",
    "has_more": false,
    "data": [
        {
            "id": "cos_1NamBL2eZvKYlo2CP38sZVEW",
            "object": "crypto.onramp_session",
            "client_secret": "cos_1NamBL2eZvKYlo2CP38sZVEW_secret_B5faamUkzHbcpjy6NndGq1mMZGGCo8FhK2P",
            "created": 1691010131,
            "kyc_details_provided": false,
            "livemode": true,
            "metadata": {},
            "redirect_url": null,
            "status": "initialized",
            "transaction_details": {
                "destination_amount": null,
                "destination_currencies": [
                    "btc",
                    "eth",
                    "matic",
                    "sol",
                    "xlm",
                    "avax",
                    "usdc"
                ],
                "destination_currency": null,
                "destination_network": null,
                "destination_networks": [
                    "bitcoin",
                    "ethereum",
                    "base",
                    "polygon",
                    "solana",
                    "stellar",
                    "avalanche"
                ],
                "fees": null,
                "
                    {
                        "id": "610a15d980d48eeaabc3e7375127cd10c8e7a6aad03ecf77d42dfd4c4f881faa",
                        "object": "crypto.onramp.quotes",
                        "destination_network_quotes": {
                            "avalanche": [
                                {
                                    "id": "dec31b3a2ef646c0bbf525774fa767097a334d51567cab715523b19e2d4a83f1",
                                    "destination_amount": "3.474296399973076273",
                                    "destination_currency": "avax",
                                    "destination_network": "avalanche",
                                    "fees": {
                                        "network_fee_monetary": "0.03",
                                        "transaction_fee_monetary": "4.04"
                                    },
                                    "source_total_amount": "104.07"
                                },
                                {
                                    "id": "3d56a9b2fdf3e5b9666461d5c28ea82ebb24287a8ece19869b02778dc70497e1",
                                    "destination_amount": "100.000000",
                                    "destination_currency": "usdc",
                                    "destination_network": "avalanche",
                                    "fees": {
                                        "network_fee_monetary": "0.06",
                                        "transaction_fee_monetary": "4.04"
                                    },
                                    "source_total_amount": "104.10"
                                }
                            ],
                            "base_network": [
                                {
                                    "id": " [
                                    {
                                        "id": "2a83796a355cfc311aec441170e2448b678828d336828c3ebb427e180e552091",
                                        "destination_amount": "0.00160673",
                                        "destination_currency": "btc",
                                        "destination_network": "bitcoin",
                                        "fees": {
                                            "network_fee_monetary": "11.89",
                                            "transaction_fee_monetary": "4.27"
                                        },
                                        "source_total_amount": "116.16"
                                    }
                            ],
                            "ethereum": [
                                {
                                    "id": "52670639e0db4e969e472b1e7e1a219fb70d8674200a5ca30bfc941a73200c82",
                                    "destination_amount": "0.029111240079494021",
                                    "destination_currency": "eth",
                                    "destination_network": "ethereum",
                                    "fees": {
                                        "network_fee_monetary": "1.25",
                                        "transaction_fee_monetary": "4.06"
                                    },
                                    "source_total_amount": "105.31"
                                },
                                {
                                    "id": "1fdae4939338d2ac2fdd2a18909cd570bdb7f412109304fb6965b826741e6f0f",
                                    "destination_amount": "100.000000",
                                    "destination_currency": "usdc",
                                    "destination_n
                                        curl https: // api.stripe.com / v1 / crypto / onramp / quotes \
                                - u "sk_test_ESDdbUTrLo4e9SC7uoQqlhd2:"
                                {
                                    "id": "610a15d980d48eeaabc3e7375127cd10c8e7a6aad03ecf77d42dfd4c4f881faa",
                                    "object": "crypto.onramp.quotes",
                                    "destination_network_quotes": {
                                        "avalanche": [
                                            {
                                                "id": "dec31b3a2ef646c0bbf525774fa767097a334d51567cab715523b19e2d4a83f1",
                                                "destination_amount": "3.474296399973076273",
                                                "destination_currency": "avax",
                                                "destination_network": "avalanche",
                                                "fees": {
                                                    "network_fee_monetary": "0.03",
                                                    "transaction_fee_monetary": "4.04"
                                                },
                                                "source_total_amount": "104.07"
                                            },
                                            {
                                                "id": "3d56a9b2fdf3e5b9666461d5c28ea82ebb24287a8ece19869b02778dc70497e1",
                                                "destination_amount": "100.000000",
                                                "destination_currency": "usdc",
                                                "destination_network": "avalanche",
                                                "fees": {
                                                    "network_fee_monetary": "0.06",
                                                    "transaction_fee_monetary": "4.04"
                                                },
                                                "source_total_amount": "104.10"
                                            }
                                        ],
                                        "base_network": [
                                            {
                                                "id": " "network_fee_monetary": "11.89",
                                                                                      "transaction_fee_monetary": "4.27"
},
"source_total_amount": "116.16"
}
],
"ethereum": [
    {
        "id": "52670639e0db4e969e472b1e7e1a219fb70d8674200a5ca30bfc941a73200c82",
        "destination_amount": "0.029111240079494021",
        "destination_currency": "eth",
        "destination_network": "ethereum",
        "fees": {
            "network_fee_monetary": "1.25",
            "transaction_fee_monetary": "4.06"
        },
        "source_total_amount": "105.31"
    },
    {
        "id": "1fdae4939338d2ac2fdd2a18909cd570bdb7f412109304fb6965b826741e6f0f",
        "destination_amount": "100.000000",
        "destination_currency": "usdc",
        "destination_network": "ethereum",
        "fees": {
            "network_fee_monetary": "3.76",
            "transaction_fee_monetary": "4.11"
        },
        "source_total_amount": "107.87"
    }
],
"polygon": [
    {
        "id": "3a039af52b
        {
            "id": "we_1Mr5jULkdIwHu7ix1ibLTM0x",
            "object": "webhook_endpoint",
            "api_version": null,
            "application": null,
            "created": 1680122196,
            "description": null,
            "enabled_events": [
                "charge.succeeded",
                "charge.failed"
            ],
            "livemode": false,
            "metadata": {},
            "secret": "whsec_wRNftLajMZNeslQOP6vEPm4iVx5NlZ6z",
            "status": "enabled",
            "url": "https://example.com/my/webhook/endpoint"
        }
            stripe webhook_endpoints create \
                                     - d "enabled_events[0]" = "charge.succeeded" \
                                                               - d
"enabled_events[1]" = "charge.failed" \
                      - -url = "https://example.com/my/webhook/endpoint"
stripe
webhook_endpoints
create \
- d
"enabled_events[0]" = "charge.succeeded" \
                      - d
"enabled_events[1]" = "charge.failed" \
                      - -url = "https://example.com/my/webhook/endpoint"

{
    "id": "we_1Mr5jULkdIwHu7ix1ibLTM0x",
    "object": "webhook_endpoint",
    "api_version": null,
    "application": null,
    "created": 1680122196,
    "description": null,
    "enabled_events": [
        "charge.succeeded",
        "charge.failed"
    ],
    "livemode": false,
    "metadata": {},
    "secret": "whsec_wRNftLajMZNeslQOP6vEPm4iVx5NlZ6z",
    "status": "enabled",
    "url": "https://example.com/my/webhook/endpoint"
}
stripe
webhook_endpoints
update
we_1Mr5jULkdIwHu7ix1ibLTM0x \
- d
"enabled_events[0]" = "charge.succeeded" \
                      - d
"enabled_events[1]" = "charge.failed" \
                      - -url = "https://example.com/new_endpoint"
{
    "id": "we_1Mr5jULkdIwHu7ix1ibLTM0x",
    "object": "webhook_endpoint",
    "api_version": null,
    "application": null,
    "created": 1680122196,
    "description": null,
    "enabled_events": [
        "charge.succeeded",
        "charge.failed"
    ],
    "livemode": false,
    "metadata": {},
    "status": "disabled",
    "url": "https://example.com/new_endpoint"
}
stripe
webhook_endpoints
retrieve
we_1Mr5jULkdIwHu7ix1ibLTM0x
{
    "id": "we_1Mr5jULkdIwHu7ix1ibLTM0x",
    "object": "webhook_endpoint",
    "api_version": null,
    "application": null,
    "created": 1680122196,
    "description": null,
    "enabled_events": [
        "charge.succeeded",
        "charge.failed"
    ],
    "livemode": false,
    "metadata": {},
    "status": "enabled",
    "url": "https://example.com/my/webhook/endpoint"
}
stripe
webhook_endpoints
list \
- -limit = 3
{
    "object": "list",
    "url": "/v1/webhook_endpoints",
    "has_more": false,
    "data": [
        {
            "id": "we_1Mr5jULkdIwHu7ix1ibLTM0x",
            "object": "webhook_endpoint",
            "api_version": null,
            "application": null,
            "created": 1680122196,
            "description": null,
            "enabled_events": [
                "charge.succeeded",
                "charge.failed"
            ],
            "livemode": false,
            "metadata": {},
            "status": "enabled",
            "url": "https://example.com/my/webhook/endpoint"
        }
        {...}
        {...}
    ],
}
stripe
webhook_endpoints
delete
we_1Mr5jULkdIwHu7ix1ibLTM0x
{
    "id": "we_1Mr5jULkdIwHu7ix1ibLTM0x",
    "object": "webhook_endpoint",
    "deleted": true
}


# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._account import Account
from stripe._customer import Customer
from stripe._deletable_api_resource import DeletableAPIResource
from stripe._error import InvalidRequestError
from stripe._expandable_field import ExpandableField
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import class_method_variant, sanitize_id
from stripe._verify_mixin import VerifyMixin
from typing import ClassVar, Dict, List, Optional, Union, cast, overload
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._card import Card


class BankAccount(
    DeletableAPIResource["BankAccount"],
    UpdateableAPIResource["BankAccount"],
    VerifyMixin,
):
    """
    These bank accounts are payment methods on `Customer` objects.

    On the other hand [External Accounts](https://stripe.com/api#external_accounts) are transfer
    destinations on `Account` objects for connected accounts.
    They can be bank accounts or debit cards as well, and are documented in the links above.

    Related guide: [Bank debits and transfers](https://stripe.com/payments/bank-debits-transfers)
    """

    OBJECT_NAME: ClassVar[Literal["bank_account"]] = "bank_account"

    class FutureRequirements(StripeObject):
        class Error(StripeObject):
            code: Literal[
                "invalid_address_city_state_postal_code",
                "invalid_address_highway_contract_box",
                "invalid_address_private_mailbox",
                "invalid_business_profile_name",
                "invalid_business_profile_name_denylisted",
                "invalid_company_name_denylisted",
                "invalid_dob_age_over_maximum",
                "invalid_dob_age_under_18",
                "invalid_dob_age_under_minimum",
                "invalid_product_description_length",
                "invalid_product_description_url_match",
                "invalid_representative_country",
                "invalid_statement_descriptor_business_mismatch",
                "invalid_statement_descriptor_denylisted",
                "invalid_statement_descriptor_length",
                "invalid_statement_descriptor_prefix_denylisted",
                "invalid_statement_descriptor_prefix_mismatch",
                "invalid_street_address",
                "invalid_tax_id",
                "invalid_tax_id_format",
                "invalid_tos_acceptance",
                "invalid_url_denylisted",
                "invalid_url_format",
                "invalid_url_length",
                "invalid_url_web_presence_detected",
                "invalid_url_website_business_information_mismatch",
                "invalid_url_website_empty",
                "invalid_url_website_inaccessible",
                "invalid_url_website_inaccessible_geoblocked",
                "invalid_url_website_inaccessible_password_protected",
                "invalid_url_website_incomplete",
                "invalid_url_website_incomplete_cancellation_policy",
                "invalid_url_website_incomplete_customer_service_details",
                "invalid_url_website_incomplete_legal_restrictions",
                "invalid_url_website_incomplete_refund_policy",
                "invalid_url_website_incomplete_return_policy",
                "invalid_url_website_incomplete_terms_and_conditions",
                "invalid_url_website_incomplete_under_construction",
                "invalid_url_website_other",
                "invalid_value_other",
                "verification_directors_mismatch",
                "verification_document_address_mismatch",
                "verification_document_address_missing",
                "verification_document_corrupt",
                "verification_document_country_not_supported",
                "verification_document_directors_mismatch",
                "verification_document_dob_mismatch",
                "verification_document_duplicate_type",
                "verification_document_expired",
                "verification_document_failed_copy",
                "verification_document_failed_greyscale",
                "verification_document_failed_other",
                "verification_document_failed_test_mode",
                "verification_document_fraudulent",
                "verification_document_id_number_mismatch",
                "verification_document_id_number_missing",
                "verification_document_incomplete",
                "verification_document_invalid",
                "verification_document_issue_or_expiry_date_missing",
                "verification_document_manipulated",
                "verification_document_missing_back",
                "verification_document_missing_front",
                "verification_document_name_mismatch",
                "verification_document_name_missing",
                "verification_document_nationality_mismatch",
                "verification_document_not_readable",
                "verification_document_not_signed",
                "verification_document_not_uploaded",
                "verification_document_photo_mismatch",
                "verification_document_too_large",
                "verification_document_type_not_supported",
                "verification_extraneous_directors",
                "verification_failed_address_match",
                "verification_failed_business_iec_number",
                "verification_failed_document_match",
                "verification_failed_id_number_match",
                "verification_failed_keyed_identity",
                "verification_failed_keyed_match",
                "verification_failed_name_match",
                "verification_failed_other",
                "verification_failed_representative_authority",
                "verification_failed_residential_address",
                "verification_failed_tax_id_match",
                "verification_failed_tax_id_not_issued",
                "verification_missing_directors",
                "verification_missing_executives",
                "verification_missing_owners",
                "verification_requires_additional_memorandum_of_associations",
                "verification_requires_additional_proof_of_registration",
            ]
            """
            The code for the type of error.
            """
            reason: str
            """
            An informative message that indicates the error type and provides additional details about the error.
            """
            requirement: str
            """
            The specific user onboarding requirement field (in the requirements hash) that needs to be resolved.
            """

        currently_due: Optional[List[str]]
        """
        Fields that need to be collected to keep the external account enabled. If not collected by `current_deadline`, these fields appear in `past_due` as well, and the account is disabled.
        """
        errors: Optional[List[Error]]
        """
        Fields that are `currently_due` and need to be collected again because validation or verification failed.
        """
        past_due: Optional[List[str]]
        """
        Fields that weren't collected by `current_deadline`. These fields need to be collected to enable the external account.
        """
        pending_verification: Optional[List[str]]
        """
        Fields that might become required depending on the results of verification or review. It's an empty array unless an asynchronous verification is pending. If verification fails, these fields move to `eventually_due`, `currently_due`, or `past_due`. Fields might appear in `eventually_due`, `currently_due`, or `past_due` and in `pending_verification` if verification fails but another verification is still pending.
        """
        _inner_class_types = {"errors": Error}

    class Requirements(StripeObject):
        class Error(StripeObject):
            code: Literal[
                "invalid_address_city_state_postal_code",
                "invalid_address_highway_contract_box",
                "invalid_address_private_mailbox",
                "invalid_business_profile_name",
                "invalid_business_profile_name_denylisted",
                "invalid_company_name_denylisted",
                "invalid_dob_age_over_maximum",
                "invalid_dob_age_under_18",
                "invalid_dob_age_under_minimum",
                "invalid_product_description_length",
                "invalid_product_description_url_match",
                "invalid_representative_country",
                "invalid_statement_descriptor_business_mismatch",
                "invalid_statement_descriptor_denylisted",
                "invalid_statement_descriptor_length",
                "invalid_statement_descriptor_prefix_denylisted",
                "invalid_statement_descriptor_prefix_mismatch",
                "invalid_street_address",
                "invalid_tax_id",
                "invalid_tax_id_format",
                "invalid_tos_acceptance",
                "invalid_url_denylisted",
                "invalid_url_format",
                "invalid_url_length",
                "invalid_url_web_presence_detected",
                "invalid_url_website_business_information_mismatch",
                "invalid_url_website_empty",
                "invalid_url_website_inaccessible",
                "invalid_url_website_inaccessible_geoblocked",
                "invalid_url_website_inaccessible_password_protected",
                "invalid_url_website_incomplete",
                "invalid_url_website_incomplete_cancellation_policy",
                "invalid_url_website_incomplete_customer_service_details",
                "invalid_url_website_incomplete_legal_restrictions",
                "invalid_url_website_incomplete_refund_policy",
                "invalid_url_website_incomplete_return_policy",
                "invalid_url_website_incomplete_terms_and_conditions",
                "invalid_url_website_incomplete_under_construction",
                "invalid_url_website_other",
                "invalid_value_other",
                "verification_directors_mismatch",
                "verification_document_address_mismatch",
                "verification_document_address_missing",
                "verification_document_corrupt",
                "verification_document_country_not_supported",
                "verification_document_directors_mismatch",
                "verification_document_dob_mismatch",
                "verification_document_duplicate_type",
                "verification_document_expired",
                "verification_document_failed_copy",
                "verification_document_failed_greyscale",
                "verification_document_failed_other",
                "verification_document_failed_test_mode",
                "verification_document_fraudulent",
                "verification_document_id_number_mismatch",
                "verification_document_id_number_missing",
                "verification_document_incomplete",
                "verification_document_invalid",
                "verification_document_issue_or_expiry_date_missing",
                "verification_document_manipulated",
                "verification_document_missing_back",
                "verification_document_missing_front",
                "verification_document_name_mismatch",
                "verification_document_name_missing",
                "verification_document_nationality_mismatch",
                "verification_document_not_readable",
                "verification_document_not_signed",
                "verification_document_not_uploaded",
                "verification_document_photo_mismatch",
                "verification_document_too_large",
                "verification_document_type_not_supported",
                "verification_extraneous_directors",
                "verification_failed_address_match",
                "verification_failed_business_iec_number",
                "verification_failed_document_match",
                "verification_failed_id_number_match",
                "verification_failed_keyed_identity",
                "verification_failed_keyed_match",
                "verification_failed_name_match",
                "verification_failed_other",
                "verification_failed_representative_authority",
                "verification_failed_residential_address",
                "verification_failed_tax_id_match",
                "verification_failed_tax_id_not_issued",
                "verification_missing_directors",
                "verification_missing_executives",
                "verification_missing_owners",
                "verification_requires_additional_memorandum_of_associations",
                "verification_requires_additional_proof_of_registration",
            ]
            """
            The code for the type of error.
            """
            reason: str
            """
            An informative message that indicates the error type and provides additional details about the error.
            """
            requirement: str
            """
            The specific user onboarding requirement field (in the requirements hash) that needs to be resolved.
            """

        currently_due: Optional[List[str]]
        """
        Fields that need to be collected to keep the external account enabled. If not collected by `current_deadline`, these fields appear in `past_due` as well, and the account is disabled.
        """
        errors: Optional[List[Error]]
        """
        Fields that are `currently_due` and need to be collected again because validation or verification failed.
        """
        past_due: Optional[List[str]]
        """
        Fields that weren't collected by `current_deadline`. These fields need to be collected to enable the external account.
        """
        pending_verification: Optional[List[str]]
        """
        Fields that might become required depending on the results of verification or review. It's an empty array unless an asynchronous verification is pending. If verification fails, these fields move to `eventually_due`, `currently_due`, or `past_due`. Fields might appear in `eventually_due`, `currently_due`, or `past_due` and in `pending_verification` if verification fails but another verification is still pending.
        """
        _inner_class_types = {"errors": Error}

    class DeleteParams(RequestOptions):
        pass

    account: Optional[ExpandableField["Account"]]
    """
    The ID of the account that the bank account is associated with.
    """
    account_holder_name: Optional[str]
    """
    The name of the person or business that owns the bank account.
    """
    account_holder_type: Optional[str]
    """
    The type of entity that holds the account. This can be either `individual` or `company`.
    """
    account_type: Optional[str]
    """
    The bank account type. This can only be `checking` or `savings` in most countries. In Japan, this can only be `futsu` or `toza`.
    """
    available_payout_methods: Optional[List[Literal["instant", "standard"]]]
    """
    A set of available payout methods for this bank account. Only values from this set should be passed as the `method` when creating a payout.
    """
    bank_name: Optional[str]
    """
    Name of the bank associated with the routing number (e.g., `WELLS FARGO`).
    """
    country: str
    """
    Two-letter ISO code representing the country the bank account is located in.
    """
    currency: str
    """
    Three-letter [ISO code for the currency](https://stripe.com/docs/payouts) paid out to the bank account.
    """
    customer: Optional[ExpandableField["Customer"]]
    """
    The ID of the customer that the bank account is associated with.
    """
    default_for_currency: Optional[bool]
    """
    Whether this bank account is the default external account for its currency.
    """
    fingerprint: Optional[str]
    """
    Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.
    """
    future_requirements: Optional[FutureRequirements]
    """
    Information about the [upcoming new requirements for the bank account](https://stripe.com/docs/connect/custom-accounts/future-requirements), including what information needs to be collected, and by when.
    """
    id: str
    """
    Unique identifier for the object.
    """
    last4: str
    """
    The last four digits of the bank account number.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["bank_account"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    requirements: Optional[Requirements]
    """
    Information about the requirements for the bank account, including what information needs to be collected.
    """
    routing_number: Optional[str]
    """
    The routing transit number for the bank account.
    """
    status: str
    """
    For bank accounts, possible values are `new`, `validated`, `verified`, `verification_failed`, or `errored`. A bank account that hasn't had any activity or validation performed is `new`. If Stripe can determine that the bank account exists, its status will be `validated`. Note that there often isn't enough information to know (e.g., for smaller credit unions), and the validation is not always run. If customer bank account verification has succeeded, the bank account status will be `verified`. If the verification failed for any reason, such as microdeposit failure, the status will be `verification_failed`. If a payout sent to this bank account fails, we'll set the status to `errored` and will not continue to send [scheduled payouts](https://stripe.com/docs/payouts#payout-schedule) until the bank details are updated.

    For external accounts, possible values are `new`, `errored` and `verification_failed`. If a payout fails, the status is set to `errored` and scheduled payouts are stopped until account details are updated. In the US and India, if we can't [verify the owner of the bank account](https://support.stripe.com/questions/bank-account-ownership-verification), we'll set the status to `verification_failed`. Other validations aren't run against external accounts because they're only used for payouts. This means the other statuses don't apply.
    """
    deleted: Optional[Literal[True]]
    """
    Always true for a deleted object
    """

    @classmethod
    def _cls_delete(
        cls, sid: str, **params: Unpack["BankAccount.DeleteParams"]
    ) -> Union["BankAccount", "Card"]:
        """
        Delete a specified external account for a given account.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(sid))
        return cast(
            Union["BankAccount", "Card"],
            cls._static_request(
                "delete",
                url,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def delete(
        sid: str, **params: Unpack["BankAccount.DeleteParams"]
    ) -> Union["BankAccount", "Card"]:
        """
        Delete a specified external account for a given account.
        """
        ...

    @overload
    def delete(
        self, **params: Unpack["BankAccount.DeleteParams"]
    ) -> Union["BankAccount", "Card"]:
        """
        Delete a specified external account for a given account.
        """
        ...

    @class_method_variant("_cls_delete")
    def delete(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["BankAccount.DeleteParams"]
    ) -> Union["BankAccount", "Card"]:
        """
        Delete a specified external account for a given account.
        """
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    async def _cls_delete_async(
        cls, sid: str, **params: Unpack["BankAccount.DeleteParams"]
    ) -> Union["BankAccount", "Card"]:
        """
        Delete a specified external account for a given account.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(sid))
        return cast(
            Union["BankAccount", "Card"],
            await cls._static_request_async(
                "delete",
                url,
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def delete_async(
        sid: str, **params: Unpack["BankAccount.DeleteParams"]
    ) -> Union["BankAccount", "Card"]:
        """
        Delete a specified external account for a given account.
        """
        ...

    @overload
    async def delete_async(
        self, **params: Unpack["BankAccount.DeleteParams"]
    ) -> Union["BankAccount", "Card"]:
        """
        Delete a specified external account for a given account.
        """
        ...

    @class_method_variant("_cls_delete_async")
    async def delete_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["BankAccount.DeleteParams"]
    ) -> Union["BankAccount", "Card"]:
        """
        Delete a specified external account for a given account.
        """
        return await self._request_and_refresh_async(
            "delete",
            self.instance_url(),
            params=params,
        )

    def instance_url(self):
        token = self.id
        extn = sanitize_id(token)
        if hasattr(self, "customer"):
            customer = self.customer

            base = Customer.class_url()
            assert customer is not None
            if isinstance(customer, Customer):
                customer = customer.id
            owner_extn = sanitize_id(customer)
            class_base = "sources"

        elif hasattr(self, "account"):
            account = self.account

            base = Account.class_url()
            assert account is not None
            if isinstance(account, Account):
                account = account.id
            owner_extn = sanitize_id(account)
            class_base = "external_accounts"

        else:
            raise InvalidRequestError(
                "Could not determine whether bank_account_id %s is "
                "attached to a customer or an account." % token,
                "id",
            )

        return "%s/%s/%s/%s" % (base, owner_extn, class_base, extn)

    @classmethod
    def modify(cls, sid, **params):
        raise NotImplementedError(
            "Can't modify a bank account without a customer or account ID. "
            "Use stripe.Customer.modify_source('customer_id', 'bank_account_id', ...) "
            "(see https://stripe.com/docs/api/customer_bank_accounts/update) or "
            "stripe.Account.modify_external_account('customer_id', 'bank_account_id', ...) "
            "(see https://stripe.com/docs/api/external_account_bank_accounts/update)."
        )

    @classmethod
    def retrieve(cls, id, **params):
        raise NotImplementedError(
            "Can't retrieve a bank account without a customer or account ID. "
            "Use stripe.customer.retrieve_source('customer_id', 'bank_account_id') "
            "(see https://stripe.com/docs/api/customer_bank_accounts/retrieve) or "
            "stripe.Account.retrieve_external_account('account_id', 'bank_account_id') "
            "(see https://stripe.com/docs/api/external_account_bank_accounts/retrieve)."
        )

    _inner_class_types = {
        "future_requirements": FutureRequirements,
        "requirements": Requirements,
    }
