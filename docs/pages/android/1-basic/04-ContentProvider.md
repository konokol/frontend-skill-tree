# ContentProvider

ContentProvider 可以帮助应用管理对自身存储或由其他应用存储的数据的访问，并提供与其他应用共享数据的方法。它们封装数据，并提供用于定义数据安全性的机制。ContentProvider 是将一个进程中的数据与另一个进程中运行的代码连接的标准接口。

实现 ContentProvider 有诸多优势。通过配置 ContentProvider，让其他应用安全地访问和修改您的应用数据。

![ContentProvider管理对存储空间的访问权限的概览图](../../../img/content-provider-overview.png)

ContentProvider对外暴露的统一的接口，业务方使用时只需要使用统一的 uri 访问数据即可，无需关系存储的实现。在ContentProvider的实现侧，数据存储可以用sqlite，文件，sharedpreference，甚至是assets。

## 使用

**自定义ContentProvider**

实现ContentProvider必须实现onCreate和增删改查方法。

```Java
public class ExampleProvider extends ContentProvider {

    // 声明数据库
    private AppDatabase appDatabase;

    // 定义DAO
    private UserDao userDao;

    private static final String DBNAME = "userdb";

    public boolean onCreate() {

        // 创建db对象
        appDatabase = Room.databaseBuilder(getContext(), AppDatabase.class, DBNAME).build();

        // 获取dao
        userDao = appDatabase.getUserDao();

        return true;
    }
    ...
    // 实现insert方法
    @Override
    public @Nullable Uri insert(@NonNull Uri uri, @Nullable ContentValues values) {
        // 这里可以使用UriMatcher来匹配Uri
    }

    //实现insert方法
    @Override
    public int update(@NonNull Uri uri, @Nullable ContentValues values,
            @Nullable String selection, @Nullable String[] selectionArgs) {
        ...
    }

    // 实现delete方法
    @Override
    public int delete(@NonNull Uri uri, @Nullable String selection,
            @Nullable String[] selectionArgs) {
        ... 
    }

    // 实现query方法
    @Override
    public @Nullable Cursor query(@NonNull Uri uri, @Nullable String[] projection,
            @Nullable String selection, @Nullable String[] selectionArgs,
            @Nullable String sortOrder) {
        ...
    }
}
```


## 原理

