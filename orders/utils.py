import string
import secrets
from .models import OrderStatus #Replace with your Coupon model when you create one

def generate_coupon_code(length=10,model=None,field_name="code",max_attempts=100):
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
    characters = string.ascii_uppercase + string.digits
    attempts=0

    while True:
        attempts +=1
        #Random Secure string generated
        coupon_code = "".join(secrets.choice(characters) for _ in range(length))

        #if model is exist
        if model:
            if not model.objects.filter(**{field_name: coupon_code}).exists():
                return coupon_code
        else:
            #model is not exist , so return code
            return coupon_code
        
        if attempts >=max_attempts:
            raise ValueError("Unable to generate a unique coupon code after maximum attempts")