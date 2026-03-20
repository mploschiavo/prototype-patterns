package org.prototypepatterns.structural.compositeentity;

import java.util.List;

public final class CompositeEntityPattern {
    private CompositeEntityPattern() {
    }

    static final class CoarseGrainedOrder {
        private String customerName = "";
        private String city = "";

        void setData(String customerName, String city) {
            this.customerName = customerName;
            this.city = city;
        }

        List<String> getData() {
            return List.of(customerName, city);
        }
    }

    public static final class CompositeOrderEntity {
        private final CoarseGrainedOrder order = new CoarseGrainedOrder();

        public void setOrder(String customerName, String city) {
            order.setData(customerName, city);
        }

        public List<String> readOrder() {
            return order.getData();
        }
    }

    public static List<String> demo() {
        CompositeOrderEntity entity = new CompositeOrderEntity();
        entity.setOrder("Sam", "Austin");
        return entity.readOrder();
    }
}
