package microservice.cart;

import javax.persistence.Id;
import java.io.Serializable;

public class CompositeKey implements Serializable {
    private int custId;
    private int itemId;
}
