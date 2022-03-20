package microservice.cart;

import org.springframework.data.repository.CrudRepository;

import java.util.List;
import java.util.Optional;

public interface CartRepository extends CrudRepository<Cart,CompositeKey> {
    List<Cart> findByCustId(String custId);
    Optional<Cart> findByCustIdAndItemId(String custId, String itemId);
//    Optional<Cart> findByCustId(String custId);
//    Cart findByCustIdAndItemId(String custId, String itemId);
}
