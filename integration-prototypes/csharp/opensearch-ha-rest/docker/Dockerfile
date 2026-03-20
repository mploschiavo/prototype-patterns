FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY src/OpenSearchHaRestService/OpenSearchHaRestService.csproj src/OpenSearchHaRestService/
RUN dotnet restore src/OpenSearchHaRestService/OpenSearchHaRestService.csproj
COPY src/OpenSearchHaRestService/ src/OpenSearchHaRestService/
RUN dotnet publish src/OpenSearchHaRestService/OpenSearchHaRestService.csproj -c Release -o /app/publish /p:UseAppHost=false
FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build /app/publish ./
ENV ASPNETCORE_URLS=http://+:8080
EXPOSE 8080
ENTRYPOINT ["dotnet", "OpenSearchHaRestService.dll"]
