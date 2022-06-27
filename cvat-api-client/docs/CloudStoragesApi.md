# cvat_api_client.CloudStoragesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudstorages_content_retrieve**](CloudStoragesApi.md#cloudstorages_content_retrieve) | **GET** /api/cloudstorages/{id}/content | Method returns a manifest content
[**cloudstorages_create**](CloudStoragesApi.md#cloudstorages_create) | **POST** /api/cloudstorages | Method creates a cloud storage with a specified characteristics
[**cloudstorages_destroy**](CloudStoragesApi.md#cloudstorages_destroy) | **DELETE** /api/cloudstorages/{id} | Method deletes a specific cloud storage
[**cloudstorages_list**](CloudStoragesApi.md#cloudstorages_list) | **GET** /api/cloudstorages | Returns a paginated list of storages according to query parameters
[**cloudstorages_partial_update**](CloudStoragesApi.md#cloudstorages_partial_update) | **PATCH** /api/cloudstorages/{id} | Methods does a partial update of chosen fields in a cloud storage instance
[**cloudstorages_preview_retrieve**](CloudStoragesApi.md#cloudstorages_preview_retrieve) | **GET** /api/cloudstorages/{id}/preview | Method returns a preview image from a cloud storage
[**cloudstorages_retrieve**](CloudStoragesApi.md#cloudstorages_retrieve) | **GET** /api/cloudstorages/{id} | Method returns details of a specific cloud storage
[**cloudstorages_status_retrieve**](CloudStoragesApi.md#cloudstorages_status_retrieve) | **GET** /api/cloudstorages/{id}/status | Method returns a cloud storage status


# **cloudstorages_content_retrieve**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} cloudstorages_content_retrieve(id)

Method returns a manifest content

### Example

* Api Key Authentication (SignatureAuthentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import time
import cvat_api_client
from cvat_api_client.api import cloud_storages_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cvat_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: SignatureAuthentication
configuration.api_key['SignatureAuthentication'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SignatureAuthentication'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = cvat_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with cvat_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_storages_api.CloudStoragesApi(api_client)
    id = 1 # int | A unique integer value identifying this cloud storage.
    manifest_path = "manifest_path_example" # str | Path to the manifest file in a cloud storage (optional)

    # example passing only required values which don't have defaults set
    try:
        # Method returns a manifest content
        api_response = api_instance.cloudstorages_content_retrieve(id)
        pprint(api_response)
    except cvat_api_client.ApiException as e:
        print("Exception when calling CloudStoragesApi->cloudstorages_content_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Method returns a manifest content
        api_response = api_instance.cloudstorages_content_retrieve(id, manifest_path=manifest_path)
        pprint(api_response)
    except cvat_api_client.ApiException as e:
        print("Exception when calling CloudStoragesApi->cloudstorages_content_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud storage. |
 **manifest_path** | **str**| Path to the manifest file in a cloud storage | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[SignatureAuthentication](../README.md#SignatureAuthentication), [basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.cvat+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A manifest content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloudstorages_create**
> CloudStorageWrite cloudstorages_create(cloud_storage_write_request)

Method creates a cloud storage with a specified characteristics

### Example

* Api Key Authentication (SignatureAuthentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import time
import cvat_api_client
from cvat_api_client.api import cloud_storages_api
from cvat_api_client.model.cloud_storage_write import CloudStorageWrite
from cvat_api_client.model.cloud_storage_write_request import CloudStorageWriteRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cvat_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: SignatureAuthentication
configuration.api_key['SignatureAuthentication'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SignatureAuthentication'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = cvat_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with cvat_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_storages_api.CloudStoragesApi(api_client)
    cloud_storage_write_request = CloudStorageWriteRequest(
        provider_type=ProviderTypeEnum("AWS_S3_BUCKET"),
        resource="resource_example",
        display_name="display_name_example",
        owner=BasicUserRequest(
            username="A",
            first_name="first_name_example",
            last_name="last_name_example",
        ),
        credentials_type=CredentialsTypeEnum("KEY_SECRET_KEY_PAIR"),
        session_token="session_token_example",
        account_name="account_name_example",
        key="key_example",
        secret_key="secret_key_example",
        key_file=open('/path/to/file', 'rb'),
        specific_attributes="specific_attributes_example",
        description="description_example",
        manifests=[
            ManifestRequest(
                filename="filename_example",
            ),
        ],
    ) # CloudStorageWriteRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Method creates a cloud storage with a specified characteristics
        api_response = api_instance.cloudstorages_create(cloud_storage_write_request)
        pprint(api_response)
    except cvat_api_client.ApiException as e:
        print("Exception when calling CloudStoragesApi->cloudstorages_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_storage_write_request** | [**CloudStorageWriteRequest**](CloudStorageWriteRequest.md)|  |

### Return type

[**CloudStorageWrite**](CloudStorageWrite.md)

### Authorization

[SignatureAuthentication](../README.md#SignatureAuthentication), [basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data, application/offset+octet-stream
 - **Accept**: application/vnd.cvat+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloudstorages_destroy**
> cloudstorages_destroy(id)

Method deletes a specific cloud storage

### Example

* Api Key Authentication (SignatureAuthentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import time
import cvat_api_client
from cvat_api_client.api import cloud_storages_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cvat_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: SignatureAuthentication
configuration.api_key['SignatureAuthentication'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SignatureAuthentication'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = cvat_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with cvat_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_storages_api.CloudStoragesApi(api_client)
    id = 1 # int | A unique integer value identifying this cloud storage.

    # example passing only required values which don't have defaults set
    try:
        # Method deletes a specific cloud storage
        api_instance.cloudstorages_destroy(id)
    except cvat_api_client.ApiException as e:
        print("Exception when calling CloudStoragesApi->cloudstorages_destroy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud storage. |

### Return type

void (empty response body)

### Authorization

[SignatureAuthentication](../README.md#SignatureAuthentication), [basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The cloud storage has been removed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloudstorages_list**
> PaginatedCloudStorageReadList cloudstorages_list()

Returns a paginated list of storages according to query parameters

### Example

* Api Key Authentication (SignatureAuthentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import time
import cvat_api_client
from cvat_api_client.api import cloud_storages_api
from cvat_api_client.model.paginated_cloud_storage_read_list import PaginatedCloudStorageReadList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cvat_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: SignatureAuthentication
configuration.api_key['SignatureAuthentication'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SignatureAuthentication'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = cvat_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with cvat_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_storages_api.CloudStoragesApi(api_client)
    filter = "filter_example" # str | A filter term. Avaliable filter_fields: ['provider_type', 'display_name', 'resource', 'credentials_type', 'owner', 'description', 'id'] (optional)
    org = "org_example" # str | Organization unique slug (optional)
    org_id = "org_id_example" # str | Organization identifier (optional)
    page = 1 # int | A page number within the paginated result set. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    search = "search_example" # str | A search term. Avaliable search_fields: ('provider_type', 'display_name', 'resource', 'credentials_type', 'owner', 'description') (optional)
    sort = "sort_example" # str | Which field to use when ordering the results. Avaliable ordering_fields: ['provider_type', 'display_name', 'resource', 'credentials_type', 'owner', 'description', 'id'] (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a paginated list of storages according to query parameters
        api_response = api_instance.cloudstorages_list(filter=filter, org=org, org_id=org_id, page=page, page_size=page_size, search=search, sort=sort)
        pprint(api_response)
    except cvat_api_client.ApiException as e:
        print("Exception when calling CloudStoragesApi->cloudstorages_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| A filter term. Avaliable filter_fields: [&#39;provider_type&#39;, &#39;display_name&#39;, &#39;resource&#39;, &#39;credentials_type&#39;, &#39;owner&#39;, &#39;description&#39;, &#39;id&#39;] | [optional]
 **org** | **str**| Organization unique slug | [optional]
 **org_id** | **str**| Organization identifier | [optional]
 **page** | **int**| A page number within the paginated result set. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **search** | **str**| A search term. Avaliable search_fields: (&#39;provider_type&#39;, &#39;display_name&#39;, &#39;resource&#39;, &#39;credentials_type&#39;, &#39;owner&#39;, &#39;description&#39;) | [optional]
 **sort** | **str**| Which field to use when ordering the results. Avaliable ordering_fields: [&#39;provider_type&#39;, &#39;display_name&#39;, &#39;resource&#39;, &#39;credentials_type&#39;, &#39;owner&#39;, &#39;description&#39;, &#39;id&#39;] | [optional]

### Return type

[**PaginatedCloudStorageReadList**](PaginatedCloudStorageReadList.md)

### Authorization

[SignatureAuthentication](../README.md#SignatureAuthentication), [basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.cvat+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloudstorages_partial_update**
> CloudStorageWrite cloudstorages_partial_update(id)

Methods does a partial update of chosen fields in a cloud storage instance

### Example

* Api Key Authentication (SignatureAuthentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import time
import cvat_api_client
from cvat_api_client.api import cloud_storages_api
from cvat_api_client.model.patched_cloud_storage_write_request import PatchedCloudStorageWriteRequest
from cvat_api_client.model.cloud_storage_write import CloudStorageWrite
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cvat_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: SignatureAuthentication
configuration.api_key['SignatureAuthentication'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SignatureAuthentication'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = cvat_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with cvat_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_storages_api.CloudStoragesApi(api_client)
    id = 1 # int | A unique integer value identifying this cloud storage.
    patched_cloud_storage_write_request = PatchedCloudStorageWriteRequest(
        provider_type=ProviderTypeEnum("AWS_S3_BUCKET"),
        resource="resource_example",
        display_name="display_name_example",
        owner=BasicUserRequest(
            username="A",
            first_name="first_name_example",
            last_name="last_name_example",
        ),
        credentials_type=CredentialsTypeEnum("KEY_SECRET_KEY_PAIR"),
        session_token="session_token_example",
        account_name="account_name_example",
        key="key_example",
        secret_key="secret_key_example",
        key_file=open('/path/to/file', 'rb'),
        specific_attributes="specific_attributes_example",
        description="description_example",
        manifests=[
            ManifestRequest(
                filename="filename_example",
            ),
        ],
    ) # PatchedCloudStorageWriteRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Methods does a partial update of chosen fields in a cloud storage instance
        api_response = api_instance.cloudstorages_partial_update(id)
        pprint(api_response)
    except cvat_api_client.ApiException as e:
        print("Exception when calling CloudStoragesApi->cloudstorages_partial_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Methods does a partial update of chosen fields in a cloud storage instance
        api_response = api_instance.cloudstorages_partial_update(id, patched_cloud_storage_write_request=patched_cloud_storage_write_request)
        pprint(api_response)
    except cvat_api_client.ApiException as e:
        print("Exception when calling CloudStoragesApi->cloudstorages_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud storage. |
 **patched_cloud_storage_write_request** | [**PatchedCloudStorageWriteRequest**](PatchedCloudStorageWriteRequest.md)|  | [optional]

### Return type

[**CloudStorageWrite**](CloudStorageWrite.md)

### Authorization

[SignatureAuthentication](../README.md#SignatureAuthentication), [basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data, application/offset+octet-stream
 - **Accept**: application/vnd.cvat+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloudstorages_preview_retrieve**
> cloudstorages_preview_retrieve(id)

Method returns a preview image from a cloud storage

### Example

* Api Key Authentication (SignatureAuthentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import time
import cvat_api_client
from cvat_api_client.api import cloud_storages_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cvat_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: SignatureAuthentication
configuration.api_key['SignatureAuthentication'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SignatureAuthentication'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = cvat_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with cvat_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_storages_api.CloudStoragesApi(api_client)
    id = 1 # int | A unique integer value identifying this cloud storage.

    # example passing only required values which don't have defaults set
    try:
        # Method returns a preview image from a cloud storage
        api_instance.cloudstorages_preview_retrieve(id)
    except cvat_api_client.ApiException as e:
        print("Exception when calling CloudStoragesApi->cloudstorages_preview_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud storage. |

### Return type

void (empty response body)

### Authorization

[SignatureAuthentication](../README.md#SignatureAuthentication), [basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cloud Storage preview |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloudstorages_retrieve**
> CloudStorageRead cloudstorages_retrieve(id)

Method returns details of a specific cloud storage

### Example

* Api Key Authentication (SignatureAuthentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import time
import cvat_api_client
from cvat_api_client.api import cloud_storages_api
from cvat_api_client.model.cloud_storage_read import CloudStorageRead
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cvat_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: SignatureAuthentication
configuration.api_key['SignatureAuthentication'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SignatureAuthentication'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = cvat_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with cvat_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_storages_api.CloudStoragesApi(api_client)
    id = 1 # int | A unique integer value identifying this cloud storage.

    # example passing only required values which don't have defaults set
    try:
        # Method returns details of a specific cloud storage
        api_response = api_instance.cloudstorages_retrieve(id)
        pprint(api_response)
    except cvat_api_client.ApiException as e:
        print("Exception when calling CloudStoragesApi->cloudstorages_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud storage. |

### Return type

[**CloudStorageRead**](CloudStorageRead.md)

### Authorization

[SignatureAuthentication](../README.md#SignatureAuthentication), [basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.cvat+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloudstorages_status_retrieve**
> str cloudstorages_status_retrieve(id)

Method returns a cloud storage status

### Example

* Api Key Authentication (SignatureAuthentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import time
import cvat_api_client
from cvat_api_client.api import cloud_storages_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cvat_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: SignatureAuthentication
configuration.api_key['SignatureAuthentication'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SignatureAuthentication'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = cvat_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with cvat_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_storages_api.CloudStoragesApi(api_client)
    id = 1 # int | A unique integer value identifying this cloud storage.

    # example passing only required values which don't have defaults set
    try:
        # Method returns a cloud storage status
        api_response = api_instance.cloudstorages_status_retrieve(id)
        pprint(api_response)
    except cvat_api_client.ApiException as e:
        print("Exception when calling CloudStoragesApi->cloudstorages_status_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud storage. |

### Return type

**str**

### Authorization

[SignatureAuthentication](../README.md#SignatureAuthentication), [basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.cvat+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cloud Storage status (AVAILABLE | NOT_FOUND | FORBIDDEN) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
