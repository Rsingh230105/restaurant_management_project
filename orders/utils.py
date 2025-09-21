import string
import secrets
from .models import OrderStatus #Replace with your Coupon model when you create one

def generate_coupon_code(length=10,model=None,field_name="code"):
    """
    Generate a unique alphanumeric coupon code.
    Args:
         length(int): Length of the coupon code. Default is 10.
         model(Model): Django model to check uniqueness against(must have the field_name)
         field_name(str): The field in the model where the code is stored.
    Returns:
           str: Unique alphanumeric coupon code.
    """

    #Define character (A-Z,a-z,0-9)
    character = string.ascii_uppercase + string.digits

    while True:
        #Random Secure string generated
        coupon_code = "".join(secrets.choice(characters) for _ in range(length))

        #Agar model diya ho to db me check kare
        if model:
            if not model.objects.filter(**{field_name: coupon_code}).exist():
                return coupon_code
        else:
            # Model nahi diya hai to bas code return karenge
            return coupon_code