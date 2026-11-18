# 并发容器与原子类

ConcurrentHashMap：JDK 1.7（分段锁）与 JDK 1.8+（CAS + synchronized 锁桶首节点）的演进；并发扩容（transfer 多线程协同搬迁）与计数（CounterCell）机制。

阻塞队列（BlockingQueue）：ArrayBlockingQueue（一把锁）与 LinkedBlockingQueue（两把锁分离）的吞吐量差异；SynchronousQueue（无缓冲直接交付）在 CachedThreadPool 中的作用。

写时复制容器：CopyOnWriteArrayList：CopyOnWriteArrayList 的适用场景（读多写少）及弱一致性迭代器问题。
