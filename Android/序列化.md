#### Implemetation
```Java
//Serializable
class SerializableObject implements Serializable {

}
```

```Java
//Parcellable
class ParcellableObject implements Parcellable {

    //A Constructor with a Parcel parameter
    ParcellableObject(Parcel in) {
        this.name = in.readString();
        this.programmingRelated = (in.readInt() == 1);
    }

    //override writeToParcel method
    @Override
    void writeToParcel(Parcel dest, int flags) {
    }

    //a creator class
    static final Parcelable.Creator<ParcellableObject> CREATOR = new Parcelable.Creator<ParcellableObject>() {

        ParcellableObject createFromParcel(Parcel in) {
            return new Skill(in);
        }

        ParcellableObject[] newArray(int size) {
            return new Skill[size];
        }
    };

    //override describeContents method
    @Override
    int describeContents() {
        return 0;
    }
}
```

#### Serializable
Serializable is a standard Java interface. You can just implement Serializable interface and add override methods. The problem with this approach is that reflection is used and it is a slow process. This method create a lot of temporary objects and cause quite a bit of garbage collection. Serializable interface is easier to implement.

Serializable是标准的Java接口。你可以只实现Serializable接口并覆写它的方法。但是通过通过Serializable接口实现序列化时会用到反射，这个过程是比较慢。同时序列化的过程中还会产生很多的临时对象，造成频繁的GC。不过好处是，这种方式实现序列化会非常简单。

#### Parcelable
Parcelable process is much faster than serializable. One of the reasons for this is that we are being explicit about the serialization process instead of using reflection to infer it. It also stands to reason that the code has been heavily optimized for this purpose.

通过Parcelable实现序列化比Serializable快很多，原因之一就是，序列化的过程是很明确的，不像Seriazable一样使用反射。同时，为了序列化，代码已经经过了很大程度的优化。

#### Conclusion

1. Parcelable is faster than Serializable interface;
2. Parcelable interface takes more time for implemetation compared to serializable interface;
3. Serializable interface is easier to implement;
4. Serializable interface create a lot of temporary objects and cause quite a bit of garbage collection;
5. Parcelable array can be pass via Intent in android;


1. Parcelable接口比Serializable更快;
2. 在实现的时候，Parcelable更麻烦，要做的事会更多;
3. Serializable接口的实现更简单；
4. Serializable在序列化是会产生很多的临时对象，造成频繁的GC;
5. Intent可以传递Parcelable数组;
